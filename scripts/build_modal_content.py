#!/usr/bin/env python3
"""Validate the modal library against the feature registry and build JSON."""

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path


FIELD_LABELS = (
    "Headline",
    "Deskripsi",
    "Yang bisa Anda lakukan",
    "Yang perlu disiapkan",
    "Hasil yang akan diperoleh",
)
FIELD_KEYS = {
    "Headline": "headline",
    "Deskripsi": "description",
    "Yang bisa Anda lakukan": "can_do",
    "Yang perlu disiapkan": "prepare",
    "Hasil yang akan diperoleh": "outcome",
}
CATEGORY_RE = re.compile(r"^## ([A-L])\. (.+)$")
FEATURE_RE = re.compile(r"^### ([0-9]+)\. (.+)$")
MARKER_RE = re.compile(r"^<!-- modal_id: ([a-z][a-z0-9]*(?:_[a-z0-9]+)*) -->$")
FIELD_RE = re.compile(
    r"^\*\*(Headline|Deskripsi|Yang bisa Anda lakukan|"
    r"Yang perlu disiapkan|Hasil yang akan diperoleh):\*\*"
)
LIBRARY_START = "# 2. Konten modal fitur"
LIBRARY_END = "# 3. Catatan penting untuk tim pengembangan"


class ValidationError(Exception):
    """Raised when source data cannot produce a complete, safe mapping."""


def _fail(message):
    raise ValidationError(message)


def _clean_field_lines(lines):
    result = list(lines)
    while result and not result[0].strip():
        result.pop(0)
    while result and not result[-1].strip():
        result.pop()
    return result


def _field_value(block_lines, start_index, end_index, label):
    match = FIELD_RE.match(block_lines[start_index])
    value_on_label_line = block_lines[start_index][match.end():]
    if value_on_label_line.startswith(" "):
        value_on_label_line = value_on_label_line[1:]
    content = [value_on_label_line] if value_on_label_line else []
    content.extend(block_lines[start_index + 1:end_index])
    content = _clean_field_lines(content)

    if not content or not any(line.strip() for line in content):
        return None

    if label == "Yang bisa Anda lakukan":
        items = []
        for line_number, line in enumerate(content, start=1):
            if not line.strip():
                continue
            if not line.startswith("- ") or not line[2:].strip():
                _fail(
                    "Field 'Yang bisa Anda lakukan' harus berisi butir '- ' "
                    f"yang tidak kosong (baris konten {line_number})."
                )
            items.append(line[2:])
        return items or None

    return "\n".join(content)


def build_payload(markdown, registry):
    """Parse and validate all source content, returning the JSON data object."""
    if not isinstance(registry, dict):
        _fail("Registry harus berupa object JSON.")
    categories = registry.get("categories")
    features = registry.get("features")
    if not isinstance(categories, list) or len(categories) != 12:
        _fail("Registry harus berisi tepat 12 kategori.")
    if not isinstance(features, list) or len(features) != 135:
        _fail("Registry harus berisi tepat 135 fitur.")

    category_ids = [item.get("id") for item in categories if isinstance(item, dict)]
    if len(category_ids) != 12 or len(set(category_ids)) != 12:
        _fail("ID kategori Registry harus lengkap dan unik.")
    category_by_order = {}
    for category in categories:
        if not isinstance(category, dict):
            _fail("Setiap kategori Registry harus berupa object.")
        order = category.get("order")
        name = category.get("name")
        if not isinstance(order, int) or order in category_by_order or not name:
            _fail("Urutan/nama kategori Registry tidak valid atau duplikat.")
        category_by_order[order] = category
    if sorted(category_by_order) != list(range(1, 13)):
        _fail("Urutan kategori Registry harus lengkap dari 1 sampai 12.")

    feature_by_number = {}
    ids = set()
    modal_ids = set()
    for feature in features:
        if not isinstance(feature, dict):
            _fail("Setiap fitur Registry harus berupa object.")
        number = feature.get("number")
        feature_id = feature.get("id")
        modal_id = feature.get("modal_id")
        if not isinstance(number, int) or number in feature_by_number:
            _fail(f"Nomor fitur Registry tidak valid atau duplikat: {number!r}.")
        if not isinstance(feature_id, str) or not re.fullmatch(
            r"[a-z][a-z0-9]*(?:_[a-z0-9]+)*", feature_id
        ):
            _fail(f"ID fitur #{number} tidak valid: {feature_id!r}.")
        if not isinstance(modal_id, str) or not MARKER_RE.fullmatch(
            f"<!-- modal_id: {modal_id} -->"
        ):
            _fail(f"modal_id fitur #{number} tidak valid: {modal_id!r}.")
        if feature_id in ids or modal_id in modal_ids:
            _fail(f"ID fitur/modal duplikat pada fitur #{number}.")
        ids.add(feature_id)
        modal_ids.add(modal_id)
        feature_by_number[number] = feature
    if sorted(feature_by_number) != list(range(1, 136)):
        _fail("Nomor fitur Registry harus lengkap dari 1 sampai 135.")

    lines = markdown.splitlines()
    try:
        content_start = lines.index(LIBRARY_START) + 1
        content_end = lines.index(LIBRARY_END, content_start)
    except ValueError as error:
        _fail(
            "Batas library modal tidak ditemukan: harus ada heading "
            f"{LIBRARY_START!r} dan {LIBRARY_END!r}."
        )

    content_lines = lines[content_start:content_end]
    category_heads = []
    feature_heads = []
    for index, line in enumerate(content_lines):
        category_match = CATEGORY_RE.fullmatch(line)
        if category_match:
            category_heads.append((index, category_match.group(1), category_match.group(2)))
        feature_match = FEATURE_RE.fullmatch(line)
        if feature_match:
            feature_heads.append((index, int(feature_match.group(1)), feature_match.group(2)))
    if len(category_heads) != 12:
        _fail(f"Library harus memiliki tepat 12 heading kategori; ditemukan {len(category_heads)}.")
    if len(feature_heads) != 135:
        _fail(f"Library harus memiliki tepat 135 heading fitur; ditemukan {len(feature_heads)}.")
    if [letter for _, letter, _ in category_heads] != list("ABCDEFGHIJKL"):
        _fail("Urutan kategori library harus berurutan dari A sampai L.")
    if [number for _, number, _ in feature_heads] != list(range(1, 136)):
        _fail("Heading fitur library harus berurutan dari 1 sampai 135.")

    marker_lines = [
        (index, line)
        for index, line in enumerate(content_lines)
        if "<!-- modal_id:" in line
    ]
    if len(marker_lines) != 135:
        _fail(
            "Library harus memiliki tepat 135 marker modal_id; "
            f"ditemukan {len(marker_lines)}."
        )
    for index, line in marker_lines:
        if not MARKER_RE.fullmatch(line):
            _fail(f"Format marker modal_id tidak valid pada baris library {index + 1}.")

    seen_marker_ids = set()
    modals = {}
    category_index = 0
    for feature_index, (heading_line, number, name) in enumerate(feature_heads):
        while (
            category_index + 1 < len(category_heads)
            and category_heads[category_index + 1][0] < heading_line
        ):
            category_index += 1
        _, category_letter, category_name = category_heads[category_index]
        category_order = ord(category_letter) - ord("A") + 1
        registry_category = category_by_order.get(category_order)
        if (
            registry_category is None
            or registry_category.get("name") != category_name
        ):
            _fail(
                f"Kategori library pada fitur #{number} ({category_name!r}) "
                "tidak cocok dengan Registry."
            )

        feature = feature_by_number.get(number)
        if feature is None:
            _fail(f"Fitur #{number} pada library tidak ada di Registry.")
        if feature.get("name") != name:
            _fail(
                f"Nama fitur #{number} berbeda: library={name!r}, "
                f"Registry={feature.get('name')!r}."
            )
        if (
            feature.get("category") != category_name
            or feature.get("category_id") != registry_category.get("id")
            or feature.get("category_order") != category_order
        ):
            _fail(f"Kategori fitur #{number} tidak cocok dengan Registry.")

        marker_line = heading_line + 1
        if marker_line >= len(content_lines):
            _fail(f"Marker modal_id hilang setelah heading fitur #{number}.")
        marker_match = MARKER_RE.fullmatch(content_lines[marker_line])
        if not marker_match:
            _fail(
                f"Marker modal_id fitur #{number} harus tepat setelah heading "
                f"dan berbentuk '<!-- modal_id: {feature.get('modal_id')} -->'."
            )
        marker_id = marker_match.group(1)
        if marker_id != feature.get("modal_id"):
            _fail(
                f"modal_id fitur #{number} tidak cocok: library={marker_id!r}, "
                f"Registry={feature.get('modal_id')!r}."
            )
        if marker_id in seen_marker_ids:
            _fail(f"Marker modal_id duplikat: {marker_id!r}.")
        seen_marker_ids.add(marker_id)

        block_end = (
            feature_heads[feature_index + 1][0]
            if feature_index + 1 < len(feature_heads)
            else len(content_lines)
        )
        block_lines = content_lines[marker_line + 1:block_end]
        while block_lines and not block_lines[-1].strip():
            block_lines.pop()
        if block_lines and block_lines[-1].strip() == "---":
            block_lines.pop()
            while block_lines and not block_lines[-1].strip():
                block_lines.pop()
        field_positions = []
        for line_index, line in enumerate(block_lines):
            match = FIELD_RE.match(line)
            if match:
                field_positions.append((line_index, match.group(1)))

        labels = [label for _, label in field_positions]
        if labels != list(FIELD_LABELS):
            missing = [label for label in FIELD_LABELS if labels.count(label) == 0]
            duplicates = [label for label in FIELD_LABELS if labels.count(label) > 1]
            _fail(
                f"Bagian fitur #{number} tidak lengkap/berurutan. "
                f"Urutan ditemukan={labels!r}; hilang={missing!r}; "
                f"duplikat={duplicates!r}."
            )

        values = {}
        for position, (start_index, label) in enumerate(field_positions):
            next_index = (
                field_positions[position + 1][0]
                if position + 1 < len(field_positions)
                else len(block_lines)
            )
            value = _field_value(block_lines, start_index, next_index, label)
            if value is None or value == "":
                _fail(f"Field {label!r} kosong pada fitur #{number}.")
            values[FIELD_KEYS[label]] = value
        modals[marker_id] = values

    if len(seen_marker_ids) != 135 or len(modals) != 135:
        _fail(
            f"Mapping harus menghasilkan 135 marker/modal; "
            f"ditemukan {len(seen_marker_ids)} marker dan {len(modals)} modal."
        )
    if seen_marker_ids != modal_ids:
        missing = sorted(modal_ids - seen_marker_ids)
        extra = sorted(seen_marker_ids - modal_ids)
        _fail(f"Set ID marker berbeda dari Registry; hilang={missing}, ekstra={extra}.")

    return {"schema_version": "1.0.0", "modals": modals}


def _atomic_write(path, payload):
    path = Path(path)
    encoded = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary_path = Path(temporary.name)
            temporary.write(encoded)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def main(argv=None):
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--markdown",
        type=Path,
        default=root / "docs/getmasteraitravelmodalcontentlibrary.md",
    )
    parser.add_argument(
        "--registry",
        type=Path,
        default=root / "docs/travelku-feature-registry.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=root / "docs/travelku-modal-content.json",
    )
    args = parser.parse_args(argv)

    try:
        markdown = args.markdown.read_text(encoding="utf-8")
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
        payload = build_payload(markdown, registry)
        _atomic_write(args.output, payload)
    except (OSError, UnicodeError, json.JSONDecodeError, ValidationError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Berhasil membuat {args.output} dengan {len(payload['modals'])} modal.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
