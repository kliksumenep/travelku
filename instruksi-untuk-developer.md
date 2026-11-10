Berikut instruksi yang bisa langsung ditempel ke GitHub Codespaces / Copilot Chat. Saya susun sebagai brief produk + spesifikasi UI/UX + alur kerja + instruksi implementasi dan pengujian.

Fokusnya: developer membangun halaman Budget Studio yang terhubung ke mesin anggaran dan menghasilkan data terstruktur untuk diteruskan ke mesin Quotation. Bukan membuat aplikasi baru, bukan mengubah mesin Quotation, dan bukan membuat generator anggaran AI yang bebas mengarang.

### INSTRUKSI DEVELOPER

### PEMBUATAN HALAMAN BUDGET STUDIO — TRAVELKU

### 1\. Tujuan Pekerjaan

Bangun halaman Budget Studio (Anggaran Proyek) pada aplikasi Travelku.

Halaman ini berfungsi untuk menyusun, mengembangkan, memeriksa, dan menetapkan anggaran suatu proyek perjalanan atau kegiatan sebelum datanya dikirim ke mesin Quotation.

Alur utama:

Data Proyek → Generate Anggaran → Review Komponen → Perhitungan → Validasi → Kirim ke Quotation

Budget Studio bukan sekadar kalkulator. Halaman ini harus mampu menampilkan komponen biaya yang sesuai dengan jenis pekerjaan, mengambil item dari Master Cost Database, menerapkan aturan Template Engine, dan menyesuaikan kedalaman pengelolaan melalui tiga level:

* Simple

* Professional

* Enterprise

Ketiga level menggunakan satu Master Cost Database dan satu Calculation Engine.

Jangan membuat database item yang terpisah untuk masing-masing level.

### 2\. Prinsip Utama Sistem

Pegang prinsip berikut selama pengembangan:

* Master Cost Database adalah sumber daftar item biaya.

* Template Engine menentukan item mana yang relevan untuk suatu proyek.

* Level menentukan kedalaman komponen, detail pengelolaan, dan tampilan.

* AI boleh membantu membaca kebutuhan, mengklasifikasikan proyek, dan merekomendasikan komponen.

* AI tidak boleh mengarang harga atau menjadi mesin hitung final.

* Perhitungan nominal harus dilakukan oleh JavaScript/application calculation engine.

* Harga yang belum tersedia harus tetap kosong, bukan otomatis Rp0.

* Perubahan level tidak boleh menghilangkan data atau pekerjaan yang sudah dimasukkan pengguna.

* Anggaran yang sudah disusun harus dapat dikirim ke mesin Quotation dalam format data yang konsisten.

* Jangan mengubah atau merusak fitur Quotation, Invoice, Kuitansi, maupun data proyek yang sudah tersimpan.

### 3\. Langkah Pertama: Audit Source Code

Sebelum menulis kode, periksa source code aktual.

Cari dan pahami:

* Struktur halaman dan navigasi aplikasi.

* Sistem penyimpanan data proyek.

* Struktur data quotation yang sudah berjalan.

* Form input proyek.

* Master data biaya jika sudah tersedia.

* Fungsi perhitungan yang sudah ada.

* Fungsi penyimpanan dan pemuatan data.

* Sistem perpindahan antarhalaman atau tab.

* Komponen UI dan CSS yang sudah digunakan.

* Fungsi yang menghubungkan anggaran dengan quotation.

Periksa apakah tabel/database yang dibutuhkan sudah tersedia. Jangan membuat tabel baru sebelum memastikan tidak ada struktur yang bisa digunakan kembali.

Aturan penting: Jangan mengubah source code pada tahap audit.

Hasil audit harus menjelaskan:

* File dan fungsi yang terkait.

* Struktur data yang sudah tersedia.

* Fitur yang dapat digunakan kembali.

* Kekurangan yang benar-benar perlu ditambahkan.

* Risiko terhadap data dan fitur lama.

* Rencana perubahan dengan lokasi kode yang jelas.

Setelah audit, susun rencana implementasi. Lakukan perubahan secara bertahap, bukan mengganti seluruh aplikasi.

### 4\. Konsep Tampilan Budget Studio

### A. Arah desain

Gunakan gaya visual Travelku yang sudah ada. Jangan membuat identitas visual baru yang terasa seperti aplikasi berbeda.

Karakter desain:

* Profesional, bersih, modern, dan mudah dipahami.

* Mobile-first, nyaman digunakan melalui HP.

* Desktop tetap optimal untuk pekerjaan anggaran yang lebih detail.

* Tidak terlalu banyak panel, garis, warna, dan ornamen.

* Hindari tombol berbentuk pil yang terlalu bulat.

* Gunakan sudut komponen sedang, bukan radius berlebihan.

* Informasi penting mudah ditemukan tanpa harus banyak menggulir.

### B. Warna

Utamakan warna yang sudah digunakan dalam aplikasi. Jika belum memiliki token warna yang konsisten, gunakan acuan berikut:

| Elemen           | Warna                   |
| ---------------- | ----------------------- |
| Warna utama      | Navy gelap #172B4D      |
| Aksen utama      | Biru #2563EB            |
| Latar halaman    | Abu sangat muda #F7F8FA |
| Permukaan kartu  | Putih #FFFFFF           |
| Teks utama       | #1F2937                 |
| Teks sekunder    | #64748B                 |
| Garis/border     | #E2E8F0                 |
| Status berhasil  | Hijau #16A34A           |
| Status perhatian | Oranye #EA580C          |
| Status kesalahan | Merah #DC2626           |

Jangan menggunakan semua warna sekaligus secara berlebihan. Warna status hanya digunakan ketika memang memiliki arti.

### C. Font

Gunakan font aplikasi yang sudah tersedia.

Jika belum ada standar, gunakan:

* Plus Jakarta Sans untuk seluruh UI.

* Judul halaman: 22–26 px desktop, 20–22 px mobile.

* Judul kartu: 15–17 px.

* Isi: 13–14 px.

* Label dan informasi pendukung: 12–13 px.

* Angka nominal: 16–20 px, gunakan font weight medium atau bold.

Pastikan nominal Rupiah mudah dibaca dan rata kanan.

### D. Bentuk komponen

* Card: putih, border tipis, radius 10–12 px.

* Input: tinggi sekitar 42–46 px.

* Tombol utama: radius 8 px, tinggi 42–46 px.

* Tombol sekunder: outline atau latar abu muda.

* Dropdown: sederhana, tidak terlalu tinggi.

* Accordion: untuk kategori biaya yang panjang.

* Modal/bottom sheet: untuk mengganti level dan menambah item.

* Sticky bottom action: untuk aksi utama pada layar mobile.

Hindari tabel lebar yang memaksa pengguna menggeser layar ke kanan. Pada HP, tampilkan item biaya sebagai kartu atau baris ringkas yang dapat dibuka untuk detail.

### 5\. Struktur Halaman dan Layout

Halaman Budget Studio memiliki enam bagian utama.

### BAGIAN 1 — Header Halaman

Tampilkan:

Budget Studio

Deskripsi:

"Susun anggaran proyek dengan komponen biaya yang sesuai kebutuhan. Mulai sederhana, kembangkan sesuai layanan yang ditawarkan."

Di bawahnya tampilkan informasi proyek:

* Nama proyek

* Nama klien

* Jenis pekerjaan

* Tanggal kegiatan

* Jumlah peserta

Informasi tersebut mengambil data dari proyek yang sedang dibuka. Jangan meminta pengguna mengisi ulang data yang sudah tersedia.

Tambahkan tombol:

* Kembali ke Proyek

* Simpan Anggaran

### BAGIAN 2 — Level Anggaran

Buat satu panel khusus dengan judul:

Level Pengelolaan Anggaran

Deskripsi:

"Sesuaikan kedalaman anggaran dengan kebutuhan dan standar layanan yang ingin ditawarkan."

Tampilkan tiga pilihan level dalam tiga kartu.

SIMPLE

Untuk perjalanan reguler dan kegiatan sederhana.

Keterangan:

* Komponen biaya utama.

* Perhitungan ringkas.

* Cocok untuk perjalanan harian dan grup kecil.

PROFESSIONAL

Untuk layanan dengan komponen lebih lengkap dan pengelolaan lebih detail.

Keterangan:

* Rincian biaya per layanan atau aktivitas.

* Pengelolaan vendor dan alternatif harga.

* Pilihan skenario layanan.

ENTERPRISE

Untuk proyek kompleks, tender, MICE besar, dan kegiatan korporasi.

Keterangan:

* RAB terperinci.

* Biaya langsung dan tidak langsung.

* Pajak, overhead, dan risiko.

* Approval, revisi, dan audit.

Tampilkan level yang sedang aktif dengan border biru dan indikator pilihan.

Tambahkan label kecil:

"Rekomendasi sistem: Professional" atau level sesuai analisis sistem.

Tombol:

Ganti Level

Perubahan level tidak boleh membuat proyek baru atau menghapus komponen sebelumnya.

Jika pengguna memilih level yang lebih tinggi, sistem menampilkan komponen tambahan yang relevan.

Jika pengguna memilih level lebih rendah, komponen tambahan tetap disimpan. Komponen tersebut dapat disembunyikan dari tampilan ringkas atau ditandai sebagai komponen lanjutan.

### BAGIAN 3 — Generate Anggaran

Tampilkan panel utama dengan judul:

Susun Komponen Anggaran

Deskripsi:

"Sistem akan memilih komponen biaya berdasarkan jenis proyek, kebutuhan peserta, aktivitas, dan level pengelolaan."

Tombol utama:

Generate Anggaran

Tambahkan informasi kecil di bawah tombol:

"Komponen diambil dari Master Cost Database dan Template Engine. Harga akan mengikuti data referensi yang tersedia."

Ketika tombol ditekan, sistem menjalankan proses:

* Membaca data proyek.

* Membaca klasifikasi pekerjaan.

* Membaca level aktif.

* Memilih template yang sesuai.

* Mengambil item dari Master Cost Database.

* Menjalankan aturan pemilihan komponen.

* Menghitung kuantitas awal jika datanya tersedia.

* Mengambil harga referensi jika tersedia dan masih layak digunakan.

* Membentuk daftar anggaran proyek.

* Menampilkan hasil agar dapat diperiksa pengguna.

Jangan membuat daftar biaya secara bebas menggunakan AI.

Jika AI digunakan untuk membantu klasifikasi, hasilnya harus tetap diarahkan ke item dan aturan yang tersedia dalam database.

Tampilkan status proses secara sederhana:

* Membaca kebutuhan proyek...

* Menentukan template...

* Memilih komponen biaya...

* Menyiapkan anggaran...

Setelah selesai, tampilkan notifikasi:

"Anggaran berhasil disusun. Silakan periksa komponen dan lengkapi harga yang belum tersedia."

### BAGIAN 4 — Daftar Komponen Anggaran

Ini merupakan bagian kerja utama.

Tampilkan kategori biaya dalam bentuk accordion.

Contoh kategori:

* Transportasi & Mobilitas

* Akomodasi

* Konsumsi & Hospitality

* Tiket Wisata & Aktivitas

* SDM, Guide & Tenaga Pelaksana

* Perlengkapan & Kebutuhan Peserta

* Produksi Acara & Dokumentasi

* Administrasi & Perizinan

* Keuangan, Komisi & Pajak

* Overhead, Risiko & Cadangan Proyek

Kategori hanya ditampilkan apabila relevan atau memiliki item yang dihasilkan. Jangan memenuhi halaman dengan kategori kosong.

Pada setiap kategori tampilkan:

* Nama kategori.

* Jumlah item.

* Subtotal kategori jika sudah dapat dihitung.

* Status kelengkapan.

Contoh tampilan item:

Bus Pariwisata

* Jumlah: 2

* Satuan: Unit

* Harga satuan: Rp ...

* Subtotal: Rp ...

* Vendor: ...

* Catatan: ...

Setiap item memiliki aksi:

* Edit

* Hapus dari anggaran

* Lihat detail

* Ganti vendor

Pengguna dapat menambahkan item melalui tombol:

\+ Tambah Komponen

Pencarian item harus mengambil data dari Master Cost Database. Jangan membuat item master baru secara otomatis hanya karena AI menyarankannya.

Jika pengguna memang membutuhkan item baru, sediakan proses penambahan item dengan aturan tersendiri dan jangan langsung mengubah master tanpa konfirmasi.

Status item:

* Wajib

* Direkomendasikan

* Kondisional

* Opsional

Status tersebut berasal dari aturan template dan harus tetap dapat dilihat pengguna.

### BAGIAN 5 — Ringkasan Perhitungan

Buat panel ringkasan yang mudah terlihat.

Judul:

Ringkasan Anggaran

Tampilkan:

* Total biaya proyek.

* Total peserta.

* Estimasi biaya per peserta.

* Harga jual per peserta jika sudah ditentukan.

* Total harga penawaran.

* Estimasi keuntungan.

* Estimasi margin.

Jangan menghitung atau menampilkan angka seolah-olah final jika komponen wajib belum lengkap.

Jika harga belum tersedia, tampilkan:

"Menunggu input harga"

Bukan Rp0.

Sediakan bagian pengaturan harga jual:

* Harga jual per orang.

* Harga jual total.

* Metode perhitungan margin/markup.

* Target margin.

* Segmentasi harga jika diperlukan.

Contohnya untuk perjalanan sekolah:

* Harga siswa.

* Harga guru.

* Guru gratis atau harga khusus.

Perhitungan harus mempertimbangkan jumlah peserta berdasarkan kelompok masing-masing. Jangan membagi total biaya dengan jumlah peserta secara otomatis jika ada kelompok yang memperoleh perlakuan harga berbeda.

### BAGIAN 6 — Validasi dan Kirim ke Quotation

Sebelum anggaran dikirim, lakukan validasi.

Judul:

Pemeriksaan Anggaran

Kelompokkan hasil menjadi:

* Wajib diperbaiki.

* Perlu diperhatikan.

* Sudah benar.

Contoh masalah:

* Harga bus belum diisi.

* Jumlah peserta belum lengkap.

* Vendor belum dipilih.

* Harga referensi sudah kedaluwarsa.

* Ada komponen duplikat.

* Kuantitas belum ditentukan.

* Pajak belum dikonfigurasi jika diperlukan.

Setiap masalah harus bisa diklik untuk membuka item yang perlu diperbaiki.

Jika semua persyaratan minimum terpenuhi, tampilkan tombol utama:

Kirim ke Quotation

Deskripsi:

"Gunakan anggaran ini sebagai dasar penyusunan penawaran harga kepada klien."

Tombol ini mengirim data anggaran yang sudah disetujui pengguna ke mesin Quotation.

Jangan mengirim data yang belum lolos validasi wajib.

### 6\. Alur Ganti Level yang Wajib Berfungsi

Contoh: pengguna awalnya membuat anggaran Simple untuk perjalanan Bu Dewi.

Kemudian pengguna memilih Professional.

Sistem harus:

* Mempertahankan seluruh item yang sudah ada.

* Membaca template dan aturan untuk Professional.

* Mengambil item tambahan yang relevan dari master.

* Memeriksa item yang sudah ada agar tidak duplikat.

* Menambahkan komponen baru yang belum tersedia.

* Menghitung kuantitas awal jika data proyek mendukung.

* Mempertahankan harga dan vendor yang sudah diinput.

* Menandai komponen yang membutuhkan pemeriksaan pengguna.

* Menghitung ulang ringkasan anggaran.

Contoh tambahan komponen Professional:

* Dokumentasi foto/video.

* Welcome kit.

* Snack box premium.

* Tour leader tambahan.

* Layanan pendampingan khusus.

* Alternatif vendor.

* Cadangan operasional.

Daftar tersebut hanya contoh. Komponen aktual harus berasal dari Master Cost Database dan aturan template.

Ketika pengguna kembali ke Simple, jangan menghapus item Professional yang sudah dibuat.

Jika pengguna sudah mengedit item atau menambahkan harga secara manual, perubahan tersebut harus tetap aman.

Tampilkan konfirmasi sebelum proses perubahan level jika sistem mendeteksi perubahan yang berpotensi mengubah struktur anggaran.

### 7\. Contoh Proyek untuk Simulasi

Gunakan proyek berikut sebagai data uji utama.

Proyek: Perjalanan Edukasi SD Muhammadiyah Magelang Kota

Data:

* Klien: Bu Dewi.

* Tujuan: Yogyakarta.

* Tanggal: 25 Desember 2026.

* Peserta: 80 orang.

* Siswa: 68 orang.

* Guru: 12 orang.

* Transportasi: 2 bus.

* Durasi: Fullday.

* Destinasi wajib: Keraton Yogyakarta.

* Destinasi tambahan: dua destinasi edukatif ramah anak.

Komponen yang perlu diperiksa:

* Bus 2 unit.

* Tol dan parkir.

* Tiket destinasi sesuai kelompok peserta.

* Makan siang.

* Snack.

* Air mineral.

* Tour guide.

* Asuransi.

* P3K.

* Operasional.

* Opsi harga khusus atau gratis untuk guru.

Simulasikan tiga kondisi:

Simulasi A — Simple

Hasilkan komponen utama perjalanan.

Simulasi B — Ganti ke Professional

Pastikan item Simple tetap ada, kemudian komponen tambahan Professional yang relevan muncul tanpa duplikasi.

Simulasi C — Kembali ke Simple

Pastikan item, harga, vendor, dan catatan yang telah diisi ketika Professional tidak hilang.

Harga yang tidak tersedia harus tetap kosong.

Jangan menggunakan harga rekaan untuk menyatakan simulasi berhasil.

### 8\. Copywriting dan Visual yang Dilihat Pengguna

Gunakan bahasa yang sederhana, langsung, dan berorientasi pada manfaat.

Hindari istilah teknis seperti Template Engine, Database Query, atau Calculation Engine pada tampilan pengguna.

Istilah teknis tersebut cukup digunakan dalam kode dan dokumentasi developer.

Gunakan copy berikut sebagai acuan:

| Lokasi             | Copy                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------- |
| Judul halaman      | Budget Studio                                                                         |
| Deskripsi          | Susun anggaran proyek dengan lebih cepat, terstruktur, dan fleksibel.                 |
| Panel level        | Sesuaikan Kedalaman Anggaran                                                          |
| Deskripsi level    | Mulai dari kebutuhan dasar hingga pengelolaan proyek yang lebih lengkap.              |
| Tombol generate    | Generate Anggaran                                                                     |
| Deskripsi generate | Komponen biaya disusun berdasarkan kebutuhan proyek dan data referensi yang tersedia. |
| Judul daftar biaya | Rincian Komponen Biaya                                                                |
| Tombol tambah      | + Tambah Komponen                                                                     |
| Ringkasan          | Ringkasan Anggaran                                                                    |
| Validasi           | Periksa Sebelum Dikirim                                                               |
| Tombol akhir       | Kirim ke Quotation                                                                    |

### Contoh visual pesan sistem

Anggaran siap dikembangkan

Anda dapat meningkatkan level anggaran kapan saja tanpa mengulang pekerjaan yang sudah dilakukan.

SimpleProfessional

Data anggaran sebelumnya tetap dipertahankan.

Beberapa harga belum diisi

Lengkapi harga komponen wajib sebelum mengirim anggaran ke Quotation.

Perlu dilengkapi

3 komponen

Visual di atas merupakan referensi pesan dan status, bukan permintaan untuk menambahkan panel dekoratif secara berlebihan.

### 9\. Struktur Data dan Integrasi Mesin Quotation

Ini bagian teknis yang paling penting.

Budget Studio harus menghasilkan struktur data yang konsisten dan bisa dibaca mesin Quotation.

Gunakan struktur proyek yang sudah tersedia jika sesuai. Jangan membuat struktur paralel yang menduplikasi data.

Secara konseptual, setiap item anggaran minimal memiliki informasi:

```js
{
  id: "project-cost-item-id",
  project_id: "project-id",
  master_cost_item_id: "master-item-id",
  category_id: "category-id",

  item_name: "Bus Pariwisata",
  quantity: 2,
  unit: "unit",
  unit_price: null,
  subtotal: null,

  vendor_id: null,
  price_source: null,
  price_date: null,

  status: "required",
  level_added: "simple",

  notes: "",
  is_active: true
}
```

Struktur tersebut adalah ilustrasi kontrak data, bukan perintah untuk langsung membuat kolom atau tabel baru. Sesuaikan dengan skema aktual setelah audit.

Data akhir anggaran minimal menyediakan:

* Identitas proyek.

* Level anggaran.

* Klasifikasi pekerjaan.

* Daftar kategori dan item.

* Kuantitas dan satuan.

* Harga satuan.

* Subtotal.

* Vendor dan sumber harga.

* Catatan dan asumsi.

* Total biaya.

* Harga jual dan margin jika sudah diatur.

* Status validasi.

* Versi anggaran.

### Kontrak output menuju Quotation

Buat satu fungsi khusus, misalnya:

```js
buildQuotationPayload(projectId)
```

Fungsi ini bertugas:

* Membaca anggaran proyek yang aktif.

* Memastikan data lolos validasi wajib.

* Menyusun item anggaran dalam struktur yang dibutuhkan Quotation.

* Mempertahankan kategori, deskripsi, jumlah, satuan, dan nominal.

* Menyertakan identitas proyek dan versi anggaran.

* Mengembalikan payload tanpa mengubah data sumber.

Contoh output konseptual:

```js
{
  project_id: "project-id",
  budget_level: "professional",
  budget_version: 1,

  items: [
    {
      description: "Bus Pariwisata",
      quantity: 2,
      unit: "unit",
      unit_price: 0,
      subtotal: 0
    }
  ],

  total_cost: 0,
  validation_status: "passed"
}
```

Perhatian: angka nol di atas hanya ilustrasi bentuk payload. Dalam implementasi, jangan mengubah harga kosong menjadi nol. Gunakan `null` atau format yang sesuai dengan kontrak mesin Quotation. Item dengan harga wajib kosong tidak boleh lolos validasi.

Jangan mengubah cara kerja mesin Quotation yang sudah berjalan sebelum memahami kontrak datanya.

Budget Studio bertugas menyediakan output yang siap diproses Quotation, bukan mengambil alih fungsi Quotation.

### 10\. Aturan Perhitungan

Pastikan aturan perhitungan konsisten:

* Subtotal item = kuantitas × harga satuan.

* Total kategori = jumlah subtotal item dalam kategori.

* Total biaya proyek = jumlah seluruh biaya aktif.

* Biaya per peserta dihitung berdasarkan segmentasi peserta yang berlaku.

* Harga jual dihitung berdasarkan metode margin atau markup yang dipilih.

* Keuntungan = harga jual total dikurangi total biaya.

* Margin harus dihitung dari basis yang benar dan diberi label dengan jelas.

Jangan menghitung subtotal apabila kuantitas atau harga belum valid.

Jangan memasukkan item yang tidak aktif dalam total.

Perubahan kuantitas, harga, vendor, dan item harus memperbarui ringkasan secara konsisten.

Hindari duplikasi fungsi perhitungan jika mesin perhitungan aplikasi sudah tersedia.

### 11\. Pengalaman Mobile dan Desktop

### Mobile

Urutan tampilan:

* Header proyek.

* Level anggaran.

* Tombol Generate Anggaran.

* Daftar kategori biaya.

* Ringkasan anggaran.

* Validasi.

* Tombol Kirim ke Quotation.

Gunakan satu kolom.

Tombol utama dapat dibuat sticky di bagian bawah, tetapi tidak boleh menutupi input atau informasi penting.

Ringkasan dapat dibuat ringkas dan diperluas ketika ditekan.

### Desktop

Gunakan layout dua kolom:

* Kolom utama: daftar komponen anggaran.

* Kolom samping: ringkasan biaya dan validasi.

Panel ringkasan dapat dibuat sticky jika tidak mengganggu.

Jangan memaksakan layout desktop dua kolom pada HP.

### 12\. Kondisi Sistem yang Harus Ditangani

Developer wajib menangani kondisi berikut:

* Proyek belum memiliki data cukup.

* Master Cost Database belum memiliki item yang cocok.

* Template belum tersedia.

* Harga item belum tersedia.

* Harga referensi sudah kedaluwarsa.

* Pengguna mengganti level.

* Pengguna menambahkan item manual.

* Pengguna menghapus item dari anggaran.

* Ada item duplikat.

* Gagal menyimpan anggaran.

* Gagal memuat data.

* Pengguna keluar sebelum menyimpan.

* Anggaran sudah dikirim ke Quotation.

* Pengguna mengubah anggaran setelah dikirim ke Quotation.

Khusus kondisi terakhir, jangan diam-diam mengubah quotation yang sudah dibuat. Terapkan mekanisme versi atau pembaruan yang sesuai dengan arsitektur aplikasi.

### 13\. Tahapan Pengerjaan Developer

Kerjakan secara berurutan.

TAHAP 1 — Audit

* Baca source aktual.

* Identifikasi komponen yang bisa digunakan kembali.

* Identifikasi struktur data dan integrasi quotation.

* Buat rencana perubahan.

Belum boleh mengubah kode.

TAHAP 2 — Kerangka UI

* Buat halaman Budget Studio.

* Buat header proyek.

* Buat pilihan level.

* Buat area Generate Anggaran.

* Buat area daftar biaya.

* Buat ringkasan dan validasi.

* Pastikan responsif mobile dan desktop.

Gunakan data dummy hanya untuk menguji tampilan, jangan simpan sebagai data proyek sungguhan.

TAHAP 3 — Integrasi Master dan Template

* Hubungkan daftar item dengan Master Cost Database.

* Terapkan pemilihan template.

* Terapkan aturan item wajib, rekomendasi, kondisional, dan opsional.

* Terapkan deduplikasi.

* Terapkan kuantitas awal sesuai data proyek.

TAHAP 4 — Ganti Level

* Implementasikan perubahan Simple, Professional, dan Enterprise.

* Pertahankan data yang sudah diinput.

* Tambahkan komponen sesuai aturan level.

* Pastikan tidak ada duplikasi.

* Uji naik level dan turun level.

TAHAP 5 — Perhitungan dan Validasi

* Hubungkan ke Calculation Engine.

* Terapkan subtotal dan total.

* Terapkan pengaturan harga jual.

* Terapkan segmentasi peserta.

* Terapkan validasi harga dan kuantitas.

TAHAP 6 — Integrasi Quotation

* Buat fungsi output payload.

* Sesuaikan dengan struktur quotation aktual.

* Uji pengiriman data.

* Pastikan dokumen quotation yang dihasilkan tidak berubah secara tidak sengaja.

TAHAP 7 — Pengujian Menyeluruh

Jalankan simulasi proyek Bu Dewi dari awal sampai akhir.

Setelah itu uji minimal satu proyek Professional dan satu proyek Enterprise.

### 14\. Standar Pengujian dan Kriteria Selesai

Pekerjaan dianggap selesai apabila:

* Halaman Budget Studio tampil baik di HP.

* Tampilan desktop tetap rapi.

* Data proyek lama dapat dimuat.

* Generate mengambil item dari master dan template.

* Harga kosong tidak dianggap nol.

* Kuantitas awal mengikuti data proyek.

* Item bisa diedit dan ditambahkan.

* Item tidak terduplikasi.

* Ganti Simple ke Professional berhasil.

* Ganti Professional ke Enterprise berhasil.

* Turun level tidak menghilangkan data.

* Ringkasan perhitungan akurat.

* Validasi bekerja.

* Data anggaran tersimpan dan dapat dimuat kembali.

* Output dapat diterima mesin Quotation.

* Quotation, Invoice, dan Kuitansi lama tetap berfungsi.

* Tidak ada error console yang belum ditangani.

* Tidak ada data proyek lama yang rusak atau hilang.

### 15\. Aturan Penting Selama Coding

* Jangan menulis ulang seluruh `index.html` atau file aplikasi tanpa alasan teknis yang terbukti.

* Jangan mengganti sistem penyimpanan yang sudah berjalan.

* Jangan mengubah database produksi tanpa audit dan rencana migrasi.

* Jangan membuat data dummy masuk ke penyimpanan proyek sebenarnya.

* Jangan mengarang harga.

* Jangan membuat tiga database berbeda untuk tiga level.

* Jangan membuat ulang mesin Quotation.

* Jangan menghapus fungsi lama yang masih digunakan.

* Gunakan fungsi dan komponen yang sudah tersedia jika memungkinkan.

* Lakukan perubahan kecil dan terukur.

Setelah setiap tahap, jalankan pengujian sebelum melanjutkan ke tahap berikutnya.

Jika ditemukan masalah pada struktur lama, laporkan dahulu penyebab dan solusi yang paling aman. Jangan langsung melakukan refactor besar.

### 16\. Format Laporan Developer

Setiap tahap harus menghasilkan laporan singkat:

* Apa yang diperiksa.

* File yang diubah.

* Fungsi yang ditambahkan atau diperbaiki.

* Bagaimana alurnya bekerja.

* Hasil pengujian.

* Masalah yang ditemukan.

* Risiko yang masih ada.

* Tahap berikutnya.

Jangan menyatakan selesai hanya karena halaman sudah terlihat bagus. Fungsionalitas, penyimpanan, perhitungan, dan integrasi Quotation harus benar-benar diuji.

HASIL AKHIR YANG DIHARAPKAN

Budget Studio menjadi ruang kerja anggaran yang mudah dipahami pengguna.

Pengguna cukup memasukkan atau menggunakan data proyek yang sudah ada, memilih level pengelolaan, lalu menekan Generate Anggaran.

Sistem menyusun komponen dari data master dan template. Pengguna memeriksa, melengkapi harga, mengatur layanan, menghitung biaya, lalu mengirim hasilnya ke mesin Quotation.

Mulai sederhana, bisa naik menjadi Professional atau Enterprise kapan saja, tanpa kehilangan pekerjaan sebelumnya.

Instruksi pertama untuk developer: jangan langsung coding. Lakukan audit source aktual terlebih dahulu, lalu kirimkan hasil audit dan rencana perubahan. Tunggu persetujuan sebelum melakukan perubahan kode.
