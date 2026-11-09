/* Travelku service worker: aplikasi tetap bisa dibuka tanpa internet.
   Strategi: jaringan dulu (selalu dapat versi terbaru), cadangan dari cache saat offline.
   Ganti nomor VERSI bila daftar ASSETS berubah. */
const VERSI = "travelku-v1";
const ASSETS = [
  "./", "index.html", "manifest.webmanifest", "icon.svg", "icon-192.png", "icon-512.png",
  "docs/travelku-feature-registry.json", "docs/travelku-modal-content.json",
  "fonts/plus-jakarta-sans-latin-wght-normal.woff2", "fonts/fraunces-latin-wght-normal.woff2"
];
self.addEventListener("install", event => {
  event.waitUntil(caches.open(VERSI).then(cache => Promise.all(ASSETS.map(url => cache.add(url).catch(() => {})))).then(() => self.skipWaiting()));
});
self.addEventListener("activate", event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSI).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", event => {
  const req = event.request;
  if (req.method !== "GET" || new URL(req.url).origin !== self.location.origin) return;
  event.respondWith(
    fetch(req).then(res => {
      if (res && res.ok) { const copy = res.clone(); caches.open(VERSI).then(c => c.put(req, copy)); }
      return res;
    }).catch(() => caches.match(req).then(hit => hit || (req.mode === "navigate" ? caches.match("index.html") : Response.error())))
  );
});
