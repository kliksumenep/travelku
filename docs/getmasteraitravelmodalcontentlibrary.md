# GetMasterAI Travel
## Library Konten Modal Seluruh Fitur
**Versi:** 1.0  
**Status:** Materi konten untuk pemasangan saat pengembangan UI  
**Bahasa:** Indonesia  
**Gaya komunikasi:** Profesional, meyakinkan, modern, ramah, berorientasi manfaat.

---

## 1. Standar tampilan modal

Saat pengguna mengeklik kartu fitur, tampilkan modal informasi terlebih dahulu. Modal ini berfungsi menjelaskan manfaat fitur dan membantu pengguna memahami apa yang akan mereka dapatkan sebelum fitur diaktifkan.

### Susunan konten modal

1. **Nama fitur** — jelas dan mudah dikenali.
2. **Headline** — kalimat singkat yang menjual manfaat utama.
3. **Deskripsi** — menjelaskan masalah yang dibantu dan nilai yang diberikan.
4. **Yang bisa Anda lakukan** — kemampuan utama fitur.
5. **Yang perlu disiapkan** — informasi atau bahan yang dibutuhkan.
6. **Hasil yang akan diperoleh** — gambaran hasil akhir.
7. **Tombol aksi** — dua tombol sejajar di bagian bawah.

### Konsep tombol

| Tombol | Posisi | Status awal | Fungsi |
|---|---|---|---|
| **Tutup** | Kiri | Aktif | Menutup modal dan kembali ke halaman sebelumnya. |
| **Buat** | Kanan | Nonaktif / disabled | Disiapkan untuk menjalankan fitur pada tahap pengembangan berikutnya. |

**Catatan implementasi:** tombol **Buat** tetap ditampilkan agar pengguna mengenali arah fungsi produk, tetapi pada versi awal dibuat nonaktif, tidak dapat diklik, dan tidak memicu proses apa pun. Jangan tampilkan pesan seolah-olah dokumen sudah dibuat. Ketika fitur sudah siap, status tombol dapat diubah menjadi aktif.

### Contoh susunan visual

```text
┌──────────────────────────────────────────┐
│  QUOTATION GENERATOR                     │
│                                          │
│  Penawaran profesional, siap dikirim     │
│                                          │
│  Susun penawaran harga dengan lebih      │
│  cepat, rapi, dan konsisten.              │
│                                          │
│  YANG BISA ANDA LAKUKAN                  │
│  • Menyusun rincian layanan               │
│  • Menghitung komponen biaya              │
│  • Menampilkan harga dan ketentuan        │
│                                          │
│  YANG PERLU DISIAPKAN                    │
│  Data pelanggan, paket, jumlah peserta,  │
│  serta komponen harga.                   │
│                                          │
│  HASIL YANG AKAN DIPEROLEH                │
│  Dokumen penawaran yang rapi dan siap    │
│  diperiksa sebelum dikirim.              │
│                                          │
│       [ Tutup ]       [ Buat ]            │
└──────────────────────────────────────────┘
```

---

# 2. Konten modal fitur

Semua konten di bawah ini disiapkan sebagai materi yang dapat dipasang ke modal masing-masing kartu fitur. Nama tombol mengikuti standar di atas: **Tutup** dan **Buat**.

## A. Dashboard

### 1. Dashboard Bisnis
<!-- modal_id: dashboard_bisnis -->
**Headline:** Seluruh aktivitas bisnis travel, terlihat dalam satu layar.

**Deskripsi:** Tidak perlu membuka banyak halaman untuk mengetahui kondisi usaha. Dashboard merangkum aktivitas penting agar Anda bisa melihat apa yang sedang berjalan, apa yang perlu ditindaklanjuti, dan apa yang membutuhkan perhatian.

**Yang bisa Anda lakukan:**
- Melihat ringkasan proyek dan perjalanan aktif.
- Memantau dokumen terbaru dan pekerjaan yang menunggu pemeriksaan.
- Melihat ringkasan tagihan dan pembayaran.
- Memantau jadwal keberangkatan mendatang.
- Mengakses pekerjaan yang paling sering digunakan.

**Yang perlu disiapkan:** Data perusahaan, proyek, dokumen, pelanggan, transaksi, dan jadwal operasional.

**Hasil yang akan diperoleh:** Gambaran aktivitas usaha yang lebih teratur untuk membantu Anda mengambil keputusan dengan cepat.

### 2. Aktivitas Terbaru
<!-- modal_id: aktivitas_terbaru -->
**Headline:** Ketahui perkembangan pekerjaan tanpa harus mencari satu per satu.

**Deskripsi:** Lihat aktivitas terbaru yang terjadi di dalam sistem. Anda dapat mengetahui dokumen yang dibuat, data yang diperbarui, dan pekerjaan yang baru saja diproses.

**Yang bisa Anda lakukan:**
- Melihat riwayat aktivitas.
- Menelusuri perubahan data dan dokumen.
- Mengetahui pekerjaan terbaru berdasarkan waktu.

**Yang perlu disiapkan:** Aktivitas pengguna dan riwayat pekerjaan di dalam sistem.

**Hasil yang akan diperoleh:** Jejak pekerjaan yang lebih mudah ditelusuri dan dipantau.

---

## B. Asisten AI

### 3. Chat Jadi Dokumen
<!-- modal_id: chat_jadi_dokumen -->
**Headline:** Dari percakapan pelanggan menjadi dokumen kerja. Lebih cepat dari cara biasa.

**Deskripsi:** Cukup masukkan percakapan atau permintaan pelanggan. AI membantu menangkap informasi penting, merapikannya, lalu menyiapkannya menjadi bahan transaksi atau dokumen yang lebih terstruktur. Anda tidak perlu memulai semuanya dari halaman kosong.

**Yang bisa Anda lakukan:**
- Memasukkan chat WhatsApp atau catatan permintaan pelanggan.
- Mengambil nama, tanggal, tujuan, jumlah peserta, dan kebutuhan layanan.
- Mengubah percakapan menjadi draft data proyek.
- Melanjutkan data ke penawaran atau dokumen terkait.

**Yang perlu disiapkan:** Chat pelanggan, catatan, atau ringkasan kebutuhan perjalanan.

**Hasil yang akan diperoleh:** Informasi pelanggan yang lebih terstruktur dan siap diperiksa sebelum diproses lebih lanjut.

### 4. Smart Data Extraction
<!-- modal_id: smart_data_extraction -->
**Headline:** Biarkan AI membaca dokumen dan menangkap data penting untuk Anda.

**Deskripsi:** Dokumen, formulir, atau catatan sering berisi banyak informasi yang harus diketik ulang. Fitur ini membantu membaca sumber informasi dan mengambil data yang relevan agar pekerjaan administrasi lebih efisien.

**Yang bisa Anda lakukan:**
- Mengambil informasi dari dokumen yang diunggah atau teks yang ditempel.
- Mengenali nama, tanggal, angka, rincian layanan, dan informasi terkait.
- Menyusun hasil ekstraksi dalam format terstruktur.
- Menandai bagian yang perlu diperiksa ulang.

**Yang perlu disiapkan:** Dokumen atau teks sumber yang informasinya ingin diambil.

**Hasil yang akan diperoleh:** Data terstruktur yang dapat diperiksa dan digunakan kembali dalam pekerjaan berikutnya.

### 5. Smart Missing Information
<!-- modal_id: smart_missing_information -->
**Headline:** Jangan sampai penawaran tertunda hanya karena ada data yang terlewat.

**Deskripsi:** AI membantu memeriksa informasi yang sudah tersedia dan menunjukkan bagian yang masih belum lengkap. Anda dapat mengetahui apa yang perlu ditanyakan kepada pelanggan sebelum menyusun penawaran atau dokumen.

**Yang bisa Anda lakukan:**
- Memeriksa kelengkapan data proyek.
- Menemukan informasi yang belum tersedia.
- Mendapatkan daftar pertanyaan klarifikasi.
- Memisahkan data yang sudah pasti dan yang masih perlu konfirmasi.

**Yang perlu disiapkan:** Data awal pelanggan atau proyek.

**Hasil yang akan diperoleh:** Daftar kekurangan informasi dan pertanyaan lanjutan agar proses kerja lebih siap.

### 6. AI Document Writer
<!-- modal_id: ai_document_writer -->
**Headline:** Susun dokumen bisnis dengan bantuan AI, tanpa mulai dari halaman kosong.

**Deskripsi:** Sampaikan tujuan dokumen dan bahan yang tersedia. AI membantu menyusun kalimat, struktur, dan isi awal dokumen agar lebih cepat mencapai draft yang layak diperiksa.

**Yang bisa Anda lakukan:**
- Menyusun draft surat dan dokumen bisnis.
- Merapikan bahasa dan struktur tulisan.
- Menyesuaikan gaya bahasa dengan kebutuhan dokumen.
- Mengembangkan catatan menjadi naskah yang lebih profesional.

**Yang perlu disiapkan:** Tujuan dokumen, informasi pendukung, dan arahan isi.

**Hasil yang akan diperoleh:** Draft dokumen yang lebih terstruktur untuk ditinjau dan disetujui.

### 7. AI Business Assistant
<!-- modal_id: ai_business_assistant -->
**Headline:** Punya partner berpikir untuk membantu mengelola bisnis travel.

**Deskripsi:** Gunakan AI untuk membantu mengembangkan ide, mengevaluasi pilihan, menyusun strategi, dan menyiapkan langkah kerja. Bukan sekadar menjawab pertanyaan, tetapi membantu Anda berpikir lebih terarah.

**Yang bisa Anda lakukan:**
- Mendiskusikan kebutuhan operasional dan pemasaran.
- Mengembangkan ide paket dan layanan.
- Menyusun rencana tindak lanjut.
- Meminta analisis awal berdasarkan data yang Anda berikan.

**Yang perlu disiapkan:** Pertanyaan, tujuan, konteks usaha, atau data pendukung.

**Hasil yang akan diperoleh:** Rekomendasi dan bahan pertimbangan yang dapat Anda evaluasi sebelum mengambil keputusan.

### 8. Auto Document Bundle
<!-- modal_id: auto_document_bundle -->
**Headline:** Satu pekerjaan, siapkan beberapa dokumen sekaligus.

**Deskripsi:** Satu proyek perjalanan sering membutuhkan banyak dokumen. Fitur ini dirancang untuk membantu menyiapkan rangkaian dokumen yang saling berkaitan dari data proyek yang sama, sehingga Anda tidak perlu memasukkan informasi berulang kali.

**Yang bisa Anda lakukan:**
- Memilih jenis dokumen yang dibutuhkan.
- Menggunakan data proyek sebagai sumber bersama.
- Menyiapkan beberapa draft dokumen dalam satu alur.
- Memeriksa konsistensi informasi antar dokumen.

**Yang perlu disiapkan:** Data proyek yang sudah cukup lengkap dan pilihan dokumen yang diperlukan.

**Hasil yang akan diperoleh:** Paket draft dokumen yang saling terhubung dan siap diperiksa.

### 9. Document Quality Check
<!-- modal_id: document_quality_check -->
**Headline:** Periksa lebih dulu. Kirim dengan lebih percaya diri.

**Deskripsi:** Kesalahan nama, tanggal, angka, atau informasi yang tidak konsisten dapat mengurangi kepercayaan pelanggan. Fitur ini membantu memeriksa kualitas isi dokumen sebelum digunakan.

**Yang bisa Anda lakukan:**
- Memeriksa kelengkapan bagian dokumen.
- Menemukan perbedaan informasi yang terlihat.
- Menandai kemungkinan salah ketik atau data yang janggal.
- Memberikan catatan untuk pemeriksaan manusia.

**Yang perlu disiapkan:** Draft dokumen dan data acuan yang benar.

**Hasil yang akan diperoleh:** Catatan pemeriksaan agar dokumen lebih rapi dan konsisten. Pemeriksaan AI bukan pengganti persetujuan manusia.

### 10. Internal & External Version
<!-- modal_id: internal_external_version -->
**Headline:** Satu proyek, dua versi dokumen sesuai kebutuhan.

**Deskripsi:** Tidak semua informasi internal perlu ditampilkan kepada pelanggan. Fitur ini membantu menyiapkan versi kerja internal dan versi eksternal yang lebih sesuai untuk dibagikan.

**Yang bisa Anda lakukan:**
- Menyusun versi internal dengan rincian operasional atau biaya.
- Menyiapkan versi pelanggan dengan informasi yang relevan.
- Memeriksa perbedaan isi kedua versi.
- Mengurangi risiko informasi internal ikut terkirim.

**Yang perlu disiapkan:** Data proyek dan aturan informasi yang boleh ditampilkan kepada pelanggan.

**Hasil yang akan diperoleh:** Draft dokumen dengan pemisahan informasi internal dan eksternal yang lebih jelas.

### 11. Document Memory
<!-- modal_id: document_memory -->
**Headline:** Data yang sudah dimasukkan bisa digunakan kembali.

**Deskripsi:** Informasi perusahaan, pelanggan, paket, dan proyek tidak seharusnya terus diketik ulang. Fitur ini dirancang agar data yang tersimpan dapat menjadi referensi saat menyiapkan pekerjaan berikutnya.

**Yang bisa Anda lakukan:**
- Menggunakan kembali data perusahaan dan pelanggan.
- Mengambil referensi paket dan layanan.
- Menelusuri dokumen atau pekerjaan terdahulu.
- Mengurangi pengisian data yang berulang.

**Yang perlu disiapkan:** Data dan dokumen yang sudah disimpan serta dikelola di sistem.

**Hasil yang akan diperoleh:** Alur kerja yang lebih efisien dengan sumber informasi yang lebih konsisten.

---

## C. Sales & Quotation

### 12. Quotation Generator
<!-- modal_id: quotation_generator -->
**Headline:** Penawaran profesional, siap diperiksa dan dikirim.

**Deskripsi:** Ubah kebutuhan pelanggan menjadi penawaran yang rapi dan mudah dipahami. Susun rincian layanan, jumlah peserta, harga, serta ketentuan dalam satu dokumen yang mencerminkan profesionalitas bisnis Anda.

**Yang bisa Anda lakukan:**
- Menyusun rincian layanan dan harga.
- Mengambil data pelanggan dan paket.
- Menampilkan ketentuan penawaran.
- Menyiapkan draft penawaran dengan identitas perusahaan.

**Yang perlu disiapkan:** Data pelanggan, paket atau layanan, jumlah peserta, harga, dan ketentuan.

**Hasil yang akan diperoleh:** Draft quotation yang siap diperiksa sebelum dikirim kepada pelanggan.

### 13. Proposal Wisata
<!-- modal_id: proposal_wisata -->
**Headline:** Tawarkan pengalaman perjalanan dengan proposal yang lebih meyakinkan.

**Deskripsi:** Proposal wisata membantu pelanggan memahami konsep perjalanan, aktivitas, fasilitas, jadwal, dan nilai layanan yang Anda tawarkan. Sajikan ide perjalanan secara lebih menarik dan profesional.

**Yang bisa Anda lakukan:**
- Menyusun konsep dan tujuan perjalanan.
- Menampilkan itinerary dan fasilitas.
- Menjelaskan layanan yang termasuk dan tidak termasuk.
- Menyajikan harga serta ketentuan penawaran.

**Yang perlu disiapkan:** Tujuan perjalanan, profil peserta, itinerary, fasilitas, harga, dan kebutuhan khusus.

**Hasil yang akan diperoleh:** Draft proposal wisata yang informatif dan siap dipresentasikan.

### 14. Travel Package Builder
<!-- modal_id: travel_package_builder -->
**Headline:** Rancang paket perjalanan yang menarik sekaligus terukur.

**Deskripsi:** Bangun produk perjalanan berdasarkan destinasi, durasi, aktivitas, transportasi, akomodasi, dan layanan pendukung. Susun paket yang mudah dipahami tim penjualan maupun calon pelanggan.

**Yang bisa Anda lakukan:**
- Menggabungkan komponen layanan menjadi paket.
- Menentukan durasi dan susunan perjalanan.
- Menyimpan detail fasilitas dan ketentuan.
- Menyiapkan deskripsi paket untuk penawaran.

**Yang perlu disiapkan:** Destinasi, layanan, durasi, fasilitas, harga dasar, dan ketentuan.

**Hasil yang akan diperoleh:** Draft paket perjalanan yang lebih terstruktur dan siap dipasarkan setelah diverifikasi.

### 15. Corporate Travel Proposal
<!-- modal_id: corporate_travel_proposal -->
**Headline:** Tampil lebih siap saat menawarkan layanan kepada perusahaan dan instansi.

**Deskripsi:** Kebutuhan perjalanan korporat biasanya memerlukan penawaran yang rinci dan tertata. Fitur ini membantu menyusun proposal dengan ruang lingkup layanan, jadwal, fasilitas, tim, dan ketentuan yang jelas.

**Yang bisa Anda lakukan:**
- Menyusun proposal perjalanan dinas atau perusahaan.
- Menampilkan ruang lingkup dan metode layanan.
- Menyusun jadwal dan kebutuhan peserta.
- Menyajikan rincian biaya dan ketentuan.

**Yang perlu disiapkan:** Profil klien, kebutuhan perjalanan, jumlah peserta, jadwal, layanan, dan biaya.

**Hasil yang akan diperoleh:** Draft proposal korporat yang lebih siap untuk proses penawaran.

### 16. RAB / Costing
<!-- modal_id: rab_costing -->
**Headline:** Ketahui struktur biaya sebelum menentukan harga jual.

**Deskripsi:** Penawaran yang menarik harus tetap sehat bagi bisnis. Susun komponen biaya secara terperinci agar Anda memahami kebutuhan anggaran, biaya per peserta, dan dasar penetapan harga.

**Yang bisa Anda lakukan:**
- Memasukkan biaya transportasi, hotel, konsumsi, tiket, kru, dan komponen lain.
- Menghitung total biaya dan biaya per peserta.
- Mengelompokkan biaya tetap dan biaya variabel.
- Meninjau asumsi serta komponen yang belum terisi.

**Yang perlu disiapkan:** Harga dari pemasok, jumlah peserta, kebutuhan layanan, dan asumsi biaya.

**Hasil yang akan diperoleh:** RAB atau costing yang lebih transparan dan dapat ditelusuri. Perhitungan mengikuti data yang dimasukkan, bukan mengarang harga pemasok.

### 17. Pricing Simulator
<!-- modal_id: pricing_simulator -->
**Headline:** Uji beberapa skenario harga sebelum menentukan penawaran terbaik.

**Deskripsi:** Perubahan jumlah peserta dan biaya dapat memengaruhi keuntungan. Simulasikan beberapa skenario untuk memahami dampaknya terhadap harga jual dan margin usaha.

**Yang bisa Anda lakukan:**
- Membandingkan skenario jumlah peserta.
- Menguji perubahan biaya.
- Menghitung harga jual berdasarkan target margin atau markup.
- Membandingkan hasil beberapa skenario.

**Yang perlu disiapkan:** Total biaya, jumlah peserta, target keuntungan, dan strategi harga.

**Hasil yang akan diperoleh:** Simulasi harga sebagai bahan keputusan sebelum penawaran diterbitkan.

### 18. Paket Gathering
<!-- modal_id: paket_gathering -->
**Headline:** Ubah kebutuhan kebersamaan menjadi paket acara yang siap ditawarkan.

**Deskripsi:** Bantu perusahaan, komunitas, dan organisasi merencanakan gathering dengan susunan kegiatan dan layanan yang jelas. Satukan kebutuhan lokasi, konsumsi, aktivitas, dan fasilitas dalam satu penawaran.

**Yang bisa Anda lakukan:**
- Menyusun konsep acara dan aktivitas.
- Memasukkan konsumsi, tempat, perlengkapan, dan fasilitator.
- Menyusun rundown dan kebutuhan peserta.
- Menghitung kebutuhan biaya.

**Yang perlu disiapkan:** Jumlah peserta, lokasi, tanggal, konsep kegiatan, konsumsi, dan fasilitas.

**Hasil yang akan diperoleh:** Draft paket gathering dan rincian penawaran yang siap ditinjau.

### 19. Paket Outbound
<!-- modal_id: paket_outbound -->
**Headline:** Rancang kegiatan outbound yang seru, terarah, dan terorganisasi.

**Deskripsi:** Susun pengalaman outbound dari tujuan kegiatan, jenis permainan, fasilitator, perlengkapan, hingga alur acara. Pastikan konsep kegiatan sesuai dengan karakter peserta dan kondisi lokasi.

**Yang bisa Anda lakukan:**
- Menentukan tujuan dan konsep aktivitas.
- Menyusun pilihan permainan dan alur kegiatan.
- Mencatat kebutuhan fasilitator dan perlengkapan.
- Menyusun rundown dan estimasi biaya.

**Yang perlu disiapkan:** Profil peserta, jumlah peserta, lokasi, tujuan kegiatan, durasi, dan kebutuhan keselamatan.

**Hasil yang akan diperoleh:** Draft paket outbound yang lebih terencana. Kelayakan aktivitas dan aspek keselamatan tetap harus diverifikasi oleh penyelenggara.

### 20. Paket Study Tour
<!-- modal_id: paket_study_tour -->
**Headline:** Susun perjalanan edukatif yang punya tujuan dan pengalaman nyata.

**Deskripsi:** Study tour bukan sekadar perjalanan. Susun tujuan pembelajaran, destinasi, jadwal kunjungan, pendamping, transportasi, dan kebutuhan peserta dalam rencana yang mudah dipahami pihak sekolah atau institusi.

**Yang bisa Anda lakukan:**
- Menyusun tujuan dan tema pembelajaran.
- Memilih destinasi dan agenda kunjungan.
- Menyiapkan itinerary dan kebutuhan pendamping.
- Menghitung biaya dan fasilitas peserta.

**Yang perlu disiapkan:** Asal peserta, jumlah peserta, tujuan edukasi, tanggal, destinasi, dan kebutuhan pendamping.

**Hasil yang akan diperoleh:** Draft paket study tour yang lebih sistematis dan siap dibahas bersama pihak pemesan.

### 21. Custom Package
<!-- modal_id: custom_package -->
**Headline:** Tidak harus memilih paket yang sudah ada. Rancang sesuai kebutuhan pelanggan.

**Deskripsi:** Setiap pelanggan bisa memiliki kebutuhan yang berbeda. Gabungkan layanan dan aktivitas sesuai permintaan untuk menghasilkan paket yang lebih relevan tanpa kehilangan kendali atas biaya dan operasional.

**Yang bisa Anda lakukan:**
- Menggabungkan layanan pilihan pelanggan.
- Menyesuaikan durasi, fasilitas, dan aktivitas.
- Menyusun opsi paket.
- Menghitung biaya berdasarkan komponen yang dipilih.

**Yang perlu disiapkan:** Permintaan pelanggan, komponen layanan, ketersediaan pemasok, dan harga terbaru.

**Hasil yang akan diperoleh:** Draft paket khusus yang sesuai kebutuhan dan siap diverifikasi.

### 22. Follow-up Letter
<!-- modal_id: follow_up_letter -->
**Headline:** Jaga peluang penjualan tetap bergerak dengan tindak lanjut yang profesional.

**Deskripsi:** Setelah penawaran dikirim, komunikasi tidak berhenti. Siapkan surat atau pesan tindak lanjut yang sopan, jelas, dan sesuai tahap pembicaraan dengan calon pelanggan.

**Yang bisa Anda lakukan:**
- Menyusun tindak lanjut setelah penawaran.
- Mengingatkan masa berlaku penawaran.
- Meminta konfirmasi atau masukan.
- Menyiapkan variasi bahasa sesuai situasi.

**Yang perlu disiapkan:** Nama pelanggan, referensi penawaran, tanggal komunikasi, dan tujuan tindak lanjut.

**Hasil yang akan diperoleh:** Draft pesan atau surat follow-up yang siap diperiksa dan dikirim.

### 23. Sales Message Generator
<!-- modal_id: sales_message_generator -->
**Headline:** Komunikasi penjualan lebih cepat, lebih tepat, dan tetap terasa personal.

**Deskripsi:** Siapkan pesan untuk memperkenalkan paket, menjawab minat calon pelanggan, mengirim penawaran, atau menindaklanjuti percakapan. Gunakan bahasa yang menarik tanpa terasa memaksa.

**Yang bisa Anda lakukan:**
- Membuat pesan promosi paket.
- Menyusun pesan pengantar penawaran.
- Membuat jawaban untuk pertanyaan calon pelanggan.
- Menyiapkan pesan follow-up dan ajakan konfirmasi.

**Yang perlu disiapkan:** Informasi produk, profil pelanggan, tujuan pesan, dan gaya komunikasi.

**Hasil yang akan diperoleh:** Draft pesan penjualan yang siap disesuaikan dan dikirim.

---

## D. Transaction & Finance

### 24. Invoice
<!-- modal_id: invoice -->
**Headline:** Tagihan resmi yang rapi membuat transaksi lebih profesional.

**Deskripsi:** Susun invoice berdasarkan data pelanggan dan proyek. Rincian layanan, nilai transaksi, nomor dokumen, dan informasi pembayaran tersaji lebih jelas.

**Yang bisa Anda lakukan:**
- Membuat draft invoice.
- Mengambil data pelanggan dan proyek.
- Menampilkan rincian tagihan dan jatuh tempo.
- Menggunakan identitas serta penomoran perusahaan.

**Yang perlu disiapkan:** Data pelanggan, rincian layanan, nilai tagihan, tanggal, dan ketentuan pembayaran.

**Hasil yang akan diperoleh:** Draft invoice yang siap diperiksa dan diterbitkan.

### 25. Invoice DP
<!-- modal_id: invoice_dp -->
**Headline:** Kelola pembayaran uang muka dengan dokumen yang jelas.

**Deskripsi:** Untuk transaksi dengan pembayaran bertahap, buat tagihan uang muka yang mencantumkan nilai DP, persentase jika digunakan, dan sisa pembayaran secara transparan.

**Yang bisa Anda lakukan:**
- Menentukan nilai atau persentase DP.
- Menampilkan total transaksi dan sisa tagihan.
- Mencantumkan batas waktu pembayaran.
- Menghubungkan DP dengan proyek terkait.

**Yang perlu disiapkan:** Nilai transaksi, ketentuan DP, data pelanggan, dan jadwal pembayaran.

**Hasil yang akan diperoleh:** Draft invoice DP yang mudah dipahami pelanggan.

### 26. Invoice Pelunasan
<!-- modal_id: invoice_pelunasan -->
**Headline:** Tahap akhir pembayaran tercatat dengan lebih tertib.

**Deskripsi:** Siapkan tagihan pelunasan berdasarkan nilai transaksi dan pembayaran yang sudah tercatat. Pastikan angka yang ditampilkan sesuai data pembayaran yang telah diverifikasi.

**Yang bisa Anda lakukan:**
- Menghitung sisa tagihan berdasarkan catatan pembayaran.
- Menampilkan pembayaran sebelumnya.
- Mencantumkan batas waktu pelunasan.
- Menghubungkan dokumen dengan invoice awal.

**Yang perlu disiapkan:** Invoice awal dan catatan pembayaran yang sudah diverifikasi.

**Hasil yang akan diperoleh:** Draft invoice pelunasan dengan rincian sisa pembayaran yang dapat ditelusuri.

### 27. Kuitansi
<!-- modal_id: kuitansi -->
**Headline:** Setiap penerimaan pembayaran memiliki bukti yang tertata.

**Deskripsi:** Buat bukti penerimaan pembayaran dengan informasi yang jelas, mulai dari pihak pembayar, jumlah, tujuan pembayaran, hingga tanggal penerimaan.

**Yang bisa Anda lakukan:**
- Menyusun kuitansi pembayaran.
- Menghubungkan kuitansi dengan proyek atau invoice.
- Menampilkan nominal angka dan terbilang.
- Menggunakan nomor kuitansi perusahaan.

**Yang perlu disiapkan:** Data pembayar, nominal, tanggal, tujuan pembayaran, dan status penerimaan yang telah dikonfirmasi.

**Hasil yang akan diperoleh:** Draft kuitansi sebagai bukti administrasi setelah penerimaan pembayaran diverifikasi.

### 28. Payment Record
<!-- modal_id: payment_record -->
**Headline:** Catat pembayaran agar posisi transaksi selalu jelas.

**Deskripsi:** Pantau pembayaran masuk berdasarkan proyek dan pelanggan. Riwayat pembayaran membantu tim memahami berapa yang sudah diterima dan berapa yang masih harus ditagih.

**Yang bisa Anda lakukan:**
- Mencatat tanggal dan nominal pembayaran.
- Menghubungkan pembayaran dengan invoice.
- Melihat status pembayaran.
- Menelusuri riwayat transaksi.

**Yang perlu disiapkan:** Bukti atau konfirmasi pembayaran, tanggal, nominal, dan referensi transaksi.

**Hasil yang akan diperoleh:** Catatan pembayaran yang lebih tertib. Input pembayaran tidak otomatis dianggap terverifikasi tanpa pemeriksaan.

### 29. Payment Reminder
<!-- modal_id: payment_reminder -->
**Headline:** Ingatkan pembayaran dengan cara yang sopan dan profesional.

**Deskripsi:** Susun pengingat pembayaran berdasarkan jatuh tempo dan status tagihan. Komunikasi yang tepat membantu menjaga arus kas sekaligus hubungan baik dengan pelanggan.

**Yang bisa Anda lakukan:**
- Menyusun pengingat sebelum jatuh tempo.
- Membuat pesan untuk tagihan yang terlambat.
- Menampilkan referensi invoice dan nominal.
- Menyesuaikan nada pesan dengan situasi pelanggan.

**Yang perlu disiapkan:** Data invoice, tanggal jatuh tempo, status pembayaran, dan kontak pelanggan.

**Hasil yang akan diperoleh:** Draft pengingat pembayaran yang siap diperiksa dan dikirim.

### 30. Expense Record
<!-- modal_id: expense_record -->
**Headline:** Catat pengeluaran proyek agar biaya tidak luput dari perhitungan.

**Deskripsi:** Pengeluaran kecil sekalipun dapat memengaruhi hasil akhir proyek. Catat biaya operasional secara teratur agar perhitungan biaya dan evaluasi proyek lebih akurat.

**Yang bisa Anda lakukan:**
- Mencatat pengeluaran berdasarkan kategori.
- Menghubungkan biaya dengan proyek.
- Menyimpan tanggal dan keterangan transaksi.
- Menambahkan referensi bukti pengeluaran.

**Yang perlu disiapkan:** Nominal, tanggal, kategori, keterangan, dan bukti transaksi jika tersedia.

**Hasil yang akan diperoleh:** Catatan pengeluaran proyek yang lebih mudah ditelusuri.

### 31. Supplier Payment
<!-- modal_id: supplier_payment -->
**Headline:** Pembayaran pemasok lebih mudah dipantau dan direkonsiliasi.

**Deskripsi:** Kelola kewajiban pembayaran kepada hotel, transportasi, restoran, dan mitra lainnya berdasarkan proyek yang terkait.

**Yang bisa Anda lakukan:**
- Mencatat tagihan pemasok.
- Mengatur tanggal jatuh tempo.
- Mencatat pembayaran yang telah dilakukan.
- Melihat sisa kewajiban per pemasok atau proyek.

**Yang perlu disiapkan:** Data pemasok, tagihan, nominal, jatuh tempo, dan bukti pembayaran.

**Hasil yang akan diperoleh:** Daftar kewajiban pemasok yang lebih terorganisasi.

### 32. Project Settlement
<!-- modal_id: project_settlement -->
**Headline:** Tutup proyek dengan angka yang jelas, bukan sekadar perkiraan.

**Deskripsi:** Setelah perjalanan selesai, rangkum pendapatan, biaya, pembayaran, dan kewajiban proyek. Gunakan hasilnya untuk mengetahui kondisi akhir pekerjaan.

**Yang bisa Anda lakukan:**
- Merangkum pendapatan proyek.
- Mengumpulkan biaya dan pembayaran pemasok.
- Membandingkan anggaran dengan realisasi.
- Menyiapkan catatan penyelesaian proyek.

**Yang perlu disiapkan:** Data transaksi, biaya aktual, pembayaran, dan dokumen pendukung.

**Hasil yang akan diperoleh:** Ringkasan penyelesaian proyek dan gambaran hasil finansial berdasarkan data yang tersedia.

### 33. Profit & Loss per Project
<!-- modal_id: profit_loss_per_project -->
**Headline:** Ketahui proyek mana yang menghasilkan keuntungan terbaik.

**Deskripsi:** Lihat hubungan antara pendapatan dan biaya pada setiap proyek. Informasi ini membantu Anda mengevaluasi harga, efisiensi operasional, dan peluang peningkatan keuntungan.

**Yang bisa Anda lakukan:**
- Menghitung pendapatan dan biaya proyek.
- Melihat laba atau rugi berdasarkan data tercatat.
- Membandingkan hasil antarproyek.
- Mengidentifikasi komponen biaya yang perlu dievaluasi.

**Yang perlu disiapkan:** Data pendapatan dan biaya yang lengkap serta telah diperiksa.

**Hasil yang akan diperoleh:** Laporan laba rugi per proyek sebagai dasar evaluasi bisnis.

---

## E. Travel Operations

### 34. Booking Confirmation
<!-- modal_id: booking_confirmation -->
**Headline:** Setelah pelanggan setuju, pastikan detail pemesanan tercatat jelas.

**Deskripsi:** Siapkan konfirmasi pemesanan yang merangkum layanan, jadwal, peserta, dan ketentuan. Dokumen ini membantu pelanggan dan tim memiliki acuan yang sama.

**Yang bisa Anda lakukan:**
- Menyusun ringkasan pemesanan.
- Menampilkan layanan dan jadwal.
- Mencantumkan status pembayaran sesuai catatan.
- Menyampaikan ketentuan penting.

**Yang perlu disiapkan:** Data proyek, pelanggan, jadwal, layanan, dan status pemesanan.

**Hasil yang akan diperoleh:** Draft konfirmasi booking yang siap diperiksa dan disampaikan.

### 35. Itinerary
<!-- modal_id: itinerary -->
**Headline:** Perjalanan tersusun rapi, dari keberangkatan hingga kembali.

**Deskripsi:** Susun jadwal perjalanan yang mudah dipahami pelanggan dan tim operasional. Atur urutan aktivitas, waktu, lokasi, serta catatan penting dalam satu dokumen.

**Yang bisa Anda lakukan:**
- Menyusun jadwal per hari atau per jam.
- Memasukkan destinasi dan aktivitas.
- Menambahkan informasi transportasi dan waktu kunjungan.
- Menyertakan catatan untuk peserta dan tim.

**Yang perlu disiapkan:** Tanggal perjalanan, rute, destinasi, durasi, dan informasi operasional.

**Hasil yang akan diperoleh:** Draft itinerary yang jelas dan siap diverifikasi dengan kondisi lapangan.

### 36. Travel Voucher
<!-- modal_id: travel_voucher -->
**Headline:** Detail layanan perjalanan tersaji jelas dalam satu voucher.

**Deskripsi:** Siapkan voucher layanan perjalanan agar pelanggan dan penyedia layanan memiliki informasi pemesanan yang sama.

**Yang bisa Anda lakukan:**
- Menyusun voucher layanan.
- Menampilkan nama peserta atau pemesan.
- Mencantumkan tanggal, lokasi, dan rincian layanan.
- Menambahkan nomor referensi pemesanan.

**Yang perlu disiapkan:** Data booking dan detail layanan yang telah dikonfirmasi.

**Hasil yang akan diperoleh:** Draft voucher perjalanan yang siap diperiksa sebelum diterbitkan.

### 37. Hotel Voucher
<!-- modal_id: hotel_voucher -->
**Headline:** Informasi akomodasi lebih jelas, mengurangi risiko salah reservasi.

**Deskripsi:** Rangkum informasi hotel dan pemesanan dalam voucher yang mudah dibaca oleh pelanggan maupun tim operasional.

**Yang bisa Anda lakukan:**
- Menampilkan nama dan alamat hotel.
- Mencantumkan tanggal check-in dan check-out.
- Menampilkan tipe kamar dan jumlah kamar.
- Menambahkan nama tamu dan nomor konfirmasi.

**Yang perlu disiapkan:** Konfirmasi resmi hotel, data tamu, tipe kamar, dan tanggal menginap.

**Hasil yang akan diperoleh:** Draft hotel voucher berdasarkan data reservasi yang telah dikonfirmasi.

### 38. Transport Voucher
<!-- modal_id: transport_voucher -->
**Headline:** Detail transportasi tercatat agar perjalanan lebih siap.

**Deskripsi:** Siapkan informasi kendaraan atau layanan transportasi yang digunakan selama perjalanan, sehingga pelanggan dan tim mengetahui detail penjemputan dan perjalanan.

**Yang bisa Anda lakukan:**
- Mencantumkan jenis kendaraan dan kapasitas.
- Menampilkan jadwal serta titik penjemputan.
- Mencatat kontak pengemudi atau operator jika tersedia.
- Menyusun detail layanan transportasi.

**Yang perlu disiapkan:** Konfirmasi kendaraan, jadwal, rute, titik jemput, dan kontak operator.

**Hasil yang akan diperoleh:** Draft transport voucher yang siap diperiksa.

### 39. Attraction Voucher
<!-- modal_id: attraction_voucher -->
**Headline:** Kunjungan destinasi lebih tertata dengan informasi yang siap dibaca.

**Deskripsi:** Rangkum tiket atau layanan aktivitas destinasi dalam voucher yang memuat detail kunjungan dan ketentuan penting.

**Yang bisa Anda lakukan:**
- Menampilkan nama destinasi atau aktivitas.
- Mencantumkan tanggal dan jumlah peserta.
- Menambahkan ketentuan kunjungan.
- Menyimpan nomor referensi jika tersedia.

**Yang perlu disiapkan:** Konfirmasi dari pengelola destinasi, tanggal, jumlah peserta, dan jenis layanan.

**Hasil yang akan diperoleh:** Draft attraction voucher yang sesuai data pemesanan.

### 40. Manifest
<!-- modal_id: manifest -->
**Headline:** Data rombongan tersusun dalam satu daftar operasional.

**Deskripsi:** Kelola daftar peserta perjalanan agar tim dapat memeriksa jumlah orang, identitas, dan kebutuhan penting sebelum keberangkatan.

**Yang bisa Anda lakukan:**
- Menyusun daftar peserta.
- Mengelompokkan peserta berdasarkan rombongan atau kendaraan.
- Menambahkan kontak darurat atau catatan relevan sesuai kebutuhan.
- Menyiapkan daftar untuk pemeriksaan keberangkatan.

**Yang perlu disiapkan:** Data peserta yang telah dikonfirmasi dan pembagian rombongan.

**Hasil yang akan diperoleh:** Draft manifest yang siap diperiksa dengan tetap menjaga kerahasiaan data pribadi peserta.

### 41. Rooming List
<!-- modal_id: rooming_list -->
**Headline:** Pembagian kamar lebih tertib, koordinasi hotel lebih mudah.

**Deskripsi:** Atur daftar tamu berdasarkan kamar, tipe kamar, dan kebutuhan akomodasi. Tim dapat meninjau pembagian kamar sebelum dikirimkan kepada pihak hotel.

**Yang bisa Anda lakukan:**
- Mengelompokkan nama tamu per kamar.
- Menentukan tipe dan jumlah kamar.
- Menambahkan catatan kebutuhan khusus.
- Menyiapkan daftar untuk konfirmasi hotel.

**Yang perlu disiapkan:** Daftar peserta, konfirmasi kamar, dan aturan pembagian kamar.

**Hasil yang akan diperoleh:** Draft rooming list yang lebih rapi dan mudah diperiksa.

### 42. Passenger List
<!-- modal_id: passenger_list -->
**Headline:** Pastikan daftar penumpang siap sebelum kendaraan berangkat.

**Deskripsi:** Susun data penumpang berdasarkan kendaraan atau rute agar proses koordinasi dan pengecekan lebih mudah.

**Yang bisa Anda lakukan:**
- Mengelompokkan penumpang per kendaraan.
- Menampilkan nama dan informasi yang diperlukan.
- Menambahkan titik naik atau turun.
- Menyiapkan daftar pemeriksaan.

**Yang perlu disiapkan:** Data peserta, pembagian kendaraan, dan informasi titik penjemputan.

**Hasil yang akan diperoleh:** Draft passenger list untuk kebutuhan operasional.

### 43. Bus Allocation
<!-- modal_id: bus_allocation -->
**Headline:** Pembagian kendaraan lebih terencana sesuai kebutuhan rombongan.

**Deskripsi:** Atur alokasi bus atau kendaraan berdasarkan jumlah peserta, kapasitas, rute, dan kebutuhan perjalanan.

**Yang bisa Anda lakukan:**
- Memasukkan daftar kendaraan dan kapasitas.
- Membagi peserta berdasarkan kendaraan.
- Menyusun informasi keberangkatan.
- Menandai kebutuhan kendaraan tambahan.

**Yang perlu disiapkan:** Jumlah peserta, data armada, kapasitas, dan rute.

**Hasil yang akan diperoleh:** Rencana alokasi kendaraan yang dapat diperiksa oleh tim operasional.

### 44. Tour Leader Assignment
<!-- modal_id: tour_leader_assignment -->
**Headline:** Setiap perjalanan memiliki penanggung jawab yang jelas.

**Deskripsi:** Tetapkan tour leader atau koordinator untuk setiap rombongan. Informasi tugas dan kontak penting dapat dibagikan kepada tim terkait.

**Yang bisa Anda lakukan:**
- Menentukan petugas per proyek atau rombongan.
- Mencatat kontak dan peran.
- Menyusun tanggung jawab utama.
- Menampilkan jadwal penugasan.

**Yang perlu disiapkan:** Data staf, jadwal, proyek, dan pembagian tugas.

**Hasil yang akan diperoleh:** Draft penugasan tim yang lebih jelas.

### 45. Rundown
<!-- modal_id: rundown -->
**Headline:** Semua pihak tahu apa yang harus dilakukan dan kapan waktunya.

**Deskripsi:** Susun alur kegiatan secara berurutan agar acara atau perjalanan berjalan lebih terkoordinasi. Setiap agenda dapat dilengkapi waktu, lokasi, penanggung jawab, dan catatan.

**Yang bisa Anda lakukan:**
- Menyusun urutan kegiatan.
- Mengatur waktu dan durasi.
- Menentukan penanggung jawab.
- Menambahkan kebutuhan perlengkapan dan catatan.

**Yang perlu disiapkan:** Konsep acara, jadwal, lokasi, tim, dan kebutuhan kegiatan.

**Hasil yang akan diperoleh:** Draft rundown yang siap dibagikan kepada tim setelah diverifikasi.

### 46. Departure Checklist
<!-- modal_id: departure_checklist -->
**Headline:** Sebelum berangkat, pastikan hal penting tidak tertinggal.

**Deskripsi:** Gunakan daftar pemeriksaan untuk membantu tim memastikan dokumen, kendaraan, peserta, perlengkapan, dan konfirmasi layanan telah siap.

**Yang bisa Anda lakukan:**
- Menyusun daftar persiapan.
- Menandai item yang sudah diperiksa.
- Menentukan penanggung jawab.
- Mencatat hal yang masih perlu diselesaikan.

**Yang perlu disiapkan:** Itinerary, manifest, voucher, daftar perlengkapan, dan kebutuhan perjalanan.

**Hasil yang akan diperoleh:** Checklist keberangkatan yang membantu mengurangi kelalaian operasional.

### 47. Trip Completion Report
<!-- modal_id: trip_completion_report -->
**Headline:** Setelah perjalanan selesai, dokumentasikan hasilnya dengan rapi.

**Deskripsi:** Rangkum pelaksanaan perjalanan, realisasi agenda, catatan layanan, dan evaluasi tim. Laporan ini dapat menjadi referensi untuk pelayanan berikutnya.

**Yang bisa Anda lakukan:**
- Mencatat realisasi perjalanan.
- Merangkum kegiatan dan layanan.
- Menambahkan catatan kendala dan evaluasi.
- Menyimpan dokumentasi pendukung.

**Yang perlu disiapkan:** Itinerary, catatan tour leader, realisasi kegiatan, dan dokumentasi.

**Hasil yang akan diperoleh:** Draft laporan penyelesaian perjalanan yang siap ditinjau.

### 48. Incident Report
<!-- modal_id: incident_report -->
**Headline:** Catat kejadian secara jelas agar tindak lanjut lebih terarah.

**Deskripsi:** Jika terjadi kendala atau insiden, dokumentasikan fakta, waktu, lokasi, pihak terkait, dan langkah penanganan. Catatan yang tertib membantu evaluasi dan komunikasi internal.

**Yang bisa Anda lakukan:**
- Mencatat waktu dan lokasi kejadian.
- Menuliskan kronologi berdasarkan fakta.
- Mencatat tindakan awal dan pihak yang menangani.
- Menambahkan tindak lanjut dan dokumen pendukung.

**Yang perlu disiapkan:** Informasi faktual, kronologi, saksi atau pihak terkait, dan bukti yang relevan.

**Hasil yang akan diperoleh:** Draft laporan insiden untuk ditinjau penanggung jawab. Fitur ini bukan pengganti prosedur darurat atau pelaporan resmi.

---

## F. Tender & Company Documents

### 49. Company Profile Builder
<!-- modal_id: company_profile_builder -->
**Headline:** Perkenalkan perusahaan dengan profil yang lebih profesional dan meyakinkan.

**Deskripsi:** Bangun profil perusahaan dari data yang sudah tersimpan. Sajikan identitas, bidang usaha, pengalaman, tim, dan keunggulan secara runtut agar calon mitra memahami kapasitas bisnis Anda.

**Yang bisa Anda lakukan:**
- Menyusun profil dan sejarah perusahaan.
- Menampilkan visi, misi, dan bidang usaha.
- Menambahkan struktur organisasi dan tim.
- Menggabungkan portofolio serta informasi pendukung.

**Yang perlu disiapkan:** Data perusahaan, legalitas, pengalaman, tim, dan identitas merek.

**Hasil yang akan diperoleh:** Draft company profile yang siap ditinjau dan disesuaikan.

### 50. Company History
<!-- modal_id: company_history -->
**Headline:** Ceritakan perjalanan perusahaan yang membangun kepercayaan.

**Deskripsi:** Susun sejarah perusahaan secara runtut, mulai dari awal berdiri, perkembangan layanan, pencapaian, hingga pengalaman penting.

**Yang bisa Anda lakukan:**
- Menyusun kronologi perkembangan perusahaan.
- Menonjolkan tonggak penting.
- Merapikan narasi sejarah.
- Menyiapkan versi singkat dan lengkap.

**Yang perlu disiapkan:** Tahun berdiri, peristiwa penting, perkembangan usaha, dan pencapaian yang dapat dibuktikan.

**Hasil yang akan diperoleh:** Narasi sejarah perusahaan yang autentik dan profesional.

### 51. Vision & Mission
<!-- modal_id: vision_mission -->
**Headline:** Tunjukkan arah perusahaan melalui visi dan misi yang jelas.

**Deskripsi:** Rumuskan arah jangka panjang dan komitmen kerja perusahaan dengan bahasa yang kuat, relevan, dan mudah dipahami.

**Yang bisa Anda lakukan:**
- Mengembangkan rumusan visi.
- Menyusun misi yang operasional.
- Menyelaraskan nilai dan arah usaha.
- Menyiapkan narasi untuk profil perusahaan.

**Yang perlu disiapkan:** Tujuan usaha, nilai perusahaan, layanan utama, dan arah pengembangan.

**Hasil yang akan diperoleh:** Draft visi dan misi yang dapat dibahas dan disahkan oleh manajemen.

### 52. Organization Chart
<!-- modal_id: organization_chart -->
**Headline:** Struktur organisasi yang jelas membuat peran dan tanggung jawab lebih mudah dipahami.

**Deskripsi:** Susun gambaran organisasi perusahaan berdasarkan jabatan, unit kerja, dan hubungan koordinasi.

**Yang bisa Anda lakukan:**
- Menyusun posisi dan jabatan.
- Mengelompokkan divisi atau fungsi kerja.
- Menampilkan garis koordinasi.
- Menyiapkan struktur untuk company profile atau proposal.

**Yang perlu disiapkan:** Daftar jabatan, nama pemangku posisi, dan hubungan pelaporan.

**Hasil yang akan diperoleh:** Draft struktur organisasi yang siap diverifikasi.

### 53. Legal Document Bank
<!-- modal_id: legal_document_bank -->
**Headline:** Simpan dokumen legalitas perusahaan secara terpusat dan mudah ditelusuri.

**Deskripsi:** Kelola dokumen penting perusahaan dalam satu tempat. Pantau versi, tanggal unggah, masa berlaku, dan status verifikasi agar dokumen lebih siap saat dibutuhkan.

**Yang bisa Anda lakukan:**
- Mengelompokkan dokumen legalitas.
- Mencatat masa berlaku dan tanggal pembaruan.
- Menandai status tersedia, perlu diperbarui, atau belum diverifikasi.
- Menelusuri dokumen berdasarkan kategori.

**Yang perlu disiapkan:** Dokumen legalitas yang sah dan informasi masa berlakunya.

**Hasil yang akan diperoleh:** Arsip legalitas yang lebih tertata. Sistem tidak membuat atau mengesahkan legalitas secara otomatis.

### 54. Portfolio Builder
<!-- modal_id: portfolio_builder -->
**Headline:** Ubah pengalaman kerja menjadi portofolio yang menunjukkan kapasitas perusahaan.

**Deskripsi:** Kumpulkan proyek, dokumentasi, klien, dan hasil pekerjaan dalam susunan yang menarik. Tampilkan pengalaman nyata sebagai bukti kemampuan perusahaan.

**Yang bisa Anda lakukan:**
- Menambahkan proyek dan pengalaman.
- Menampilkan foto atau dokumentasi.
- Menyusun ringkasan ruang lingkup pekerjaan.
- Memilih proyek untuk profil atau proposal.

**Yang perlu disiapkan:** Data proyek, periode, klien yang boleh disebut, dokumentasi, dan bukti pendukung.

**Hasil yang akan diperoleh:** Draft portofolio berdasarkan pengalaman yang benar-benar dimiliki perusahaan.

### 55. Project Experience List
<!-- modal_id: project_experience_list -->
**Headline:** Tampilkan rekam jejak proyek secara terstruktur dan mudah diperiksa.

**Deskripsi:** Susun daftar pengalaman pekerjaan dengan informasi yang konsisten agar mudah digunakan untuk proposal, company profile, maupun kebutuhan tender.

**Yang bisa Anda lakukan:**
- Mencatat nama dan periode proyek.
- Menampilkan klien dan ruang lingkup pekerjaan.
- Mencatat nilai atau skala proyek jika dapat dipublikasikan.
- Mengelompokkan pengalaman berdasarkan jenis layanan.

**Yang perlu disiapkan:** Data proyek dan bukti pengalaman yang dapat diverifikasi.

**Hasil yang akan diperoleh:** Daftar pengalaman perusahaan yang rapi dan siap dipilih sesuai kebutuhan.

### 56. Certificate Archive
<!-- modal_id: certificate_archive -->
**Headline:** Sertifikat dan kompetensi tersimpan, masa berlakunya terpantau.

**Deskripsi:** Kelola sertifikat perusahaan maupun personel agar dokumen kompetensi lebih mudah ditemukan saat dibutuhkan.

**Yang bisa Anda lakukan:**
- Mengarsipkan sertifikat berdasarkan kategori.
- Mencatat pemilik dan tanggal berlaku.
- Menandai dokumen yang perlu diperbarui.
- Menelusuri sertifikat berdasarkan nama atau jenis.

**Yang perlu disiapkan:** Salinan sertifikat dan informasi penerbit serta masa berlaku.

**Hasil yang akan diperoleh:** Arsip sertifikat yang lebih terorganisasi dan siap diperiksa.

### 57. Team & CV Builder
<!-- modal_id: team_cv_builder -->
**Headline:** Perkenalkan tim yang membuat layanan perusahaan dapat diandalkan.

**Deskripsi:** Susun profil personel dan CV secara konsisten untuk kebutuhan company profile, proposal, atau tender.

**Yang bisa Anda lakukan:**
- Menyusun profil tenaga ahli dan staf.
- Menampilkan pengalaman dan kompetensi.
- Mengatur peran dalam proyek.
- Menyiapkan format CV yang seragam.

**Yang perlu disiapkan:** Data personel, pengalaman, pendidikan, sertifikat, dan persetujuan penggunaan data.

**Hasil yang akan diperoleh:** Draft profil tim dan CV yang siap diperiksa oleh masing-masing personel.

### 58. Partner & Supplier Profile
<!-- modal_id: partner_supplier_profile -->
**Headline:** Data mitra tersusun rapi untuk mendukung kesiapan operasional.

**Deskripsi:** Kelola informasi hotel, transportasi, restoran, destinasi, dan pemasok lainnya agar tim lebih mudah menemukan mitra yang sesuai.

**Yang bisa Anda lakukan:**
- Menyimpan identitas dan kontak mitra.
- Mengelompokkan mitra berdasarkan layanan.
- Mencatat area layanan dan informasi kerja sama.
- Menyimpan dokumen pendukung yang tersedia.

**Yang perlu disiapkan:** Data mitra, kontak, jenis layanan, dan dokumen kerja sama jika ada.

**Hasil yang akan diperoleh:** Direktori mitra yang lebih mudah digunakan dalam perencanaan proyek.

### 59. Tender Requirement Reader
<!-- modal_id: tender_requirement_reader -->
**Headline:** Baca persyaratan tender lebih cepat dan ketahui apa saja yang diminta.

**Deskripsi:** Dokumen tender sering panjang dan memiliki banyak persyaratan. AI membantu membaca dokumen, merangkum kebutuhan, dan mengidentifikasi dokumen yang harus disiapkan.

**Yang bisa Anda lakukan:**
- Membaca dokumen persyaratan tender.
- Mengidentifikasi daftar dokumen administrasi dan teknis.
- Menangkap tenggat dan ketentuan penting.
- Menyusun ringkasan persyaratan untuk diperiksa.

**Yang perlu disiapkan:** Dokumen tender atau kerangka acuan yang resmi dan lengkap.

**Hasil yang akan diperoleh:** Ringkasan dan daftar persyaratan berdasarkan dokumen sumber. Hasil AI tetap harus dibandingkan dengan dokumen tender asli.

### 60. Tender Checklist
<!-- modal_id: tender_checklist -->
**Headline:** Pantau kesiapan tender, satu persyaratan demi satu persyaratan.

**Deskripsi:** Cocokkan persyaratan tender dengan dokumen yang dimiliki perusahaan. Ketahui mana yang tersedia, belum tersedia, kedaluwarsa, atau masih perlu diverifikasi.

**Yang bisa Anda lakukan:**
- Membuat daftar persyaratan tender.
- Mencocokkan dengan arsip perusahaan.
- Menandai status setiap dokumen.
- Melihat pekerjaan yang masih harus diselesaikan.

**Yang perlu disiapkan:** Dokumen tender dan arsip perusahaan.

**Hasil yang akan diperoleh:** Checklist kesiapan tender yang membantu tim bekerja lebih sistematis.

### 61. Tender Document Pack
<!-- modal_id: tender_document_pack -->
**Headline:** Kumpulkan dokumen tender dalam satu paket yang lebih teratur.

**Deskripsi:** Setelah persyaratan dipetakan, pilih dokumen yang relevan dan susun urutannya sesuai kebutuhan tender. Tim dapat memeriksa kelengkapan sebelum paket digunakan.

**Yang bisa Anda lakukan:**
- Memilih dokumen dari bank dokumen.
- Mengelompokkan dokumen administrasi dan pendukung.
- Menyusun urutan sesuai persyaratan.
- Memeriksa status versi dan masa berlaku.

**Yang perlu disiapkan:** Persyaratan tender dan dokumen perusahaan yang valid.

**Hasil yang akan diperoleh:** Paket draft dokumen tender yang siap diperiksa secara menyeluruh sebelum pengajuan.

### 62. Technical Proposal Builder
<!-- modal_id: technical_proposal_builder -->
**Headline:** Susun gagasan teknis menjadi proposal yang runtut dan meyakinkan.

**Deskripsi:** Bangun proposal teknis dari pemahaman kebutuhan klien, metode pelaksanaan, jadwal, tim, hingga pengendalian risiko. Sajikan solusi dengan struktur yang mudah dievaluasi.

**Yang bisa Anda lakukan:**
- Menyusun pemahaman kebutuhan pekerjaan.
- Menjelaskan metodologi dan tahapan.
- Menyusun jadwal, tim, dan pembagian tugas.
- Menambahkan standar layanan dan mitigasi risiko.

**Yang perlu disiapkan:** Dokumen kebutuhan pekerjaan, kapasitas perusahaan, metode kerja, dan data tim.

**Hasil yang akan diperoleh:** Draft proposal teknis yang sesuai bahan dan kemampuan nyata perusahaan.

### 63. Tender Cover Letter
<!-- modal_id: tender_cover_letter -->
**Headline:** Awali pengajuan penawaran dengan surat pengantar yang profesional.

**Deskripsi:** Siapkan surat pengantar penawaran dengan identitas perusahaan, tujuan surat, referensi paket pekerjaan, dan daftar lampiran yang relevan.

**Yang bisa Anda lakukan:**
- Menyusun surat pengantar.
- Memasukkan informasi tender.
- Menampilkan daftar lampiran.
- Menggunakan format dan penomoran perusahaan.

**Yang perlu disiapkan:** Identitas perusahaan, informasi tender, pihak tujuan, dan daftar dokumen.

**Hasil yang akan diperoleh:** Draft surat pengantar yang siap diperiksa dan ditandatangani pejabat berwenang.

### 64. Statement Letter Generator
<!-- modal_id: statement_letter_generator -->
**Headline:** Siapkan surat pernyataan sesuai kebutuhan administrasi pekerjaan.

**Deskripsi:** Bantu menyusun draft surat pernyataan berdasarkan format dan persyaratan yang diminta. Setiap pernyataan harus sesuai keadaan sebenarnya dan diperiksa sebelum ditandatangani.

**Yang bisa Anda lakukan:**
- Menyusun draft surat pernyataan.
- Menyesuaikan format dengan kebutuhan dokumen.
- Memasukkan identitas dan referensi pekerjaan.
- Menyiapkan ruang tanda tangan.

**Yang perlu disiapkan:** Persyaratan resmi, data perusahaan, dan fakta yang akan dinyatakan.

**Hasil yang akan diperoleh:** Draft surat pernyataan untuk diperiksa dan disahkan oleh pihak berwenang. AI tidak boleh mengarang fakta atau komitmen perusahaan.

### 65. Expiry Alerts
<!-- modal_id: expiry_alerts -->
**Headline:** Jangan sampai dokumen penting kedaluwarsa saat sedang dibutuhkan.

**Deskripsi:** Pantau masa berlaku dokumen perusahaan dan sertifikat. Pengingat membantu tim merencanakan pembaruan lebih awal.

**Yang bisa Anda lakukan:**
- Mencatat tanggal kedaluwarsa.
- Mengelompokkan dokumen berdasarkan masa berlaku.
- Melihat dokumen yang mendekati jatuh tempo.
- Menyiapkan daftar tindak lanjut pembaruan.

**Yang perlu disiapkan:** Tanggal berlaku dan kedaluwarsa dari dokumen yang benar.

**Hasil yang akan diperoleh:** Daftar pemantauan masa berlaku dokumen yang lebih tertib.

---

## G. Proposal Builder

### 66. Proposal Cover
<!-- modal_id: proposal_cover -->
**Headline:** Kesan pertama proposal dimulai dari sampul yang profesional.

**Deskripsi:** Siapkan halaman sampul dengan identitas perusahaan, judul pekerjaan, nama klien, dan elemen visual yang konsisten dengan merek Anda.

**Yang bisa Anda lakukan:**
- Menentukan judul dan subjudul.
- Memasukkan logo dan identitas perusahaan.
- Menampilkan nama klien dan tanggal.
- Memilih gaya sampul yang sesuai.

**Yang perlu disiapkan:** Logo, identitas perusahaan, judul proposal, dan data klien.

**Hasil yang akan diperoleh:** Draft sampul proposal yang siap digabungkan dengan isi dokumen.

### 67. Cover Letter
<!-- modal_id: cover_letter -->
**Headline:** Sampaikan penawaran dengan pembuka yang tepat dan berkelas.

**Deskripsi:** Susun surat pengantar yang menjelaskan maksud pengajuan, konteks kebutuhan klien, dan komitmen perusahaan secara ringkas.

**Yang bisa Anda lakukan:**
- Menyusun surat pengantar proposal.
- Menyesuaikan penerima dan tujuan.
- Menjelaskan ringkasan penawaran.
- Menambahkan penutup dan kontak perusahaan.

**Yang perlu disiapkan:** Data klien, tujuan proposal, dan ringkasan layanan.

**Hasil yang akan diperoleh:** Draft surat pengantar yang siap ditinjau dan ditandatangani.

### 68. Executive Summary
<!-- modal_id: executive_summary -->
**Headline:** Sampaikan inti proposal dalam ringkasan yang langsung dipahami.

**Deskripsi:** Bantu pembaca memahami kebutuhan, solusi, manfaat, dan gambaran penawaran tanpa harus membaca seluruh dokumen terlebih dahulu.

**Yang bisa Anda lakukan:**
- Merangkum kebutuhan klien.
- Menjelaskan solusi yang ditawarkan.
- Menampilkan manfaat utama.
- Merangkum ruang lingkup dan nilai penawaran.

**Yang perlu disiapkan:** Informasi kebutuhan klien dan isi utama proposal.

**Hasil yang akan diperoleh:** Ringkasan eksekutif yang padat, jelas, dan meyakinkan.

### 69. Client Needs Understanding
<!-- modal_id: client_needs_understanding -->
**Headline:** Tunjukkan bahwa Anda memahami kebutuhan klien, bukan sekadar menjual layanan.

**Deskripsi:** Rumuskan kebutuhan dan tantangan klien berdasarkan informasi yang diberikan. Bagian ini menjadi dasar untuk menjelaskan mengapa solusi yang ditawarkan relevan.

**Yang bisa Anda lakukan:**
- Merangkum kebutuhan utama.
- Mengelompokkan tujuan dan tantangan.
- Menandai asumsi yang perlu dikonfirmasi.
- Menghubungkan kebutuhan dengan solusi.

**Yang perlu disiapkan:** Brief, hasil diskusi, atau dokumen kebutuhan klien.

**Hasil yang akan diperoleh:** Draft pemahaman kebutuhan klien yang dapat dikonfirmasi sebelum proposal dilanjutkan.

### 70. Solution Description
<!-- modal_id: solution_description -->
**Headline:** Jelaskan solusi yang membuat penawaran Anda layak dipilih.

**Deskripsi:** Susun penjelasan layanan sebagai jawaban atas kebutuhan klien. Fokus pada manfaat, ruang lingkup, dan nilai tambah yang benar-benar dapat diberikan.

**Yang bisa Anda lakukan:**
- Menjelaskan solusi utama.
- Menghubungkan layanan dengan kebutuhan.
- Menyusun manfaat dan keunggulan.
- Memisahkan layanan utama dan tambahan.

**Yang perlu disiapkan:** Kebutuhan klien, kapasitas perusahaan, dan rincian layanan.

**Hasil yang akan diperoleh:** Draft bagian solusi yang relevan dan tidak berlebihan dalam menjanjikan kemampuan.

### 71. Methodology
<!-- modal_id: methodology -->
**Headline:** Tunjukkan bagaimana pekerjaan akan dilaksanakan, tahap demi tahap.

**Deskripsi:** Jelaskan metode kerja agar klien memahami proses, koordinasi, dan standar pelaksanaan yang direncanakan.

**Yang bisa Anda lakukan:**
- Menyusun tahapan kerja.
- Menjelaskan metode koordinasi.
- Menentukan peran dan tanggung jawab.
- Menambahkan mekanisme evaluasi.

**Yang perlu disiapkan:** Ruang lingkup pekerjaan, metode operasional, dan kapasitas tim.

**Hasil yang akan diperoleh:** Draft metodologi pelaksanaan yang runtut dan realistis.

### 72. Work Plan
<!-- modal_id: work_plan -->
**Headline:** Ubah rencana menjadi tahapan kerja yang terukur.

**Deskripsi:** Susun aktivitas, penanggung jawab, kebutuhan, dan target waktu agar pelaksanaan pekerjaan lebih mudah dipantau.

**Yang bisa Anda lakukan:**
- Membagi pekerjaan menjadi beberapa tahap.
- Menentukan aktivitas dan keluaran.
- Menetapkan penanggung jawab.
- Menyusun target waktu.

**Yang perlu disiapkan:** Ruang lingkup, jadwal, tim, dan target pekerjaan.

**Hasil yang akan diperoleh:** Draft rencana kerja yang dapat digunakan sebagai acuan koordinasi.

### 73. Schedule Builder
<!-- modal_id: schedule_builder -->
**Headline:** Jadwal yang jelas membantu semua pihak bergerak selaras.

**Deskripsi:** Susun jadwal kegiatan atau pelaksanaan pekerjaan dalam format yang mudah dibaca dan diperbarui.

**Yang bisa Anda lakukan:**
- Menyusun tanggal dan waktu kegiatan.
- Mengatur durasi dan urutan aktivitas.
- Menandai agenda penting.
- Menyiapkan jadwal untuk proposal atau operasional.

**Yang perlu disiapkan:** Tanggal, durasi, agenda, dan batasan waktu.

**Hasil yang akan diperoleh:** Draft jadwal yang siap dikonfirmasi dengan pihak terkait.

### 74. Proposal Itinerary
<!-- modal_id: proposal_itinerary -->
**Headline:** Gambarkan pengalaman perjalanan sebelum pelanggan memutuskan.

**Deskripsi:** Sajikan rencana perjalanan secara menarik dan informatif agar pelanggan dapat memahami alur pengalaman yang ditawarkan.

**Yang bisa Anda lakukan:**
- Menyusun agenda perjalanan.
- Menjelaskan destinasi dan aktivitas.
- Menambahkan estimasi waktu.
- Menyajikan catatan fasilitas dan layanan.

**Yang perlu disiapkan:** Rute, destinasi, durasi, aktivitas, dan informasi layanan.

**Hasil yang akan diperoleh:** Draft itinerary untuk kebutuhan proposal yang siap diverifikasi.

### 75. Team Presentation
<!-- modal_id: team_presentation -->
**Headline:** Perlihatkan siapa yang akan menjalankan pekerjaan.

**Deskripsi:** Tampilkan personel dan peran yang relevan agar klien memahami struktur pelaksana dan kompetensi tim.

**Yang bisa Anda lakukan:**
- Menampilkan personel kunci.
- Menjelaskan peran dan tanggung jawab.
- Memasukkan ringkasan pengalaman.
- Menyusun struktur tim proyek.

**Yang perlu disiapkan:** Data personel, persetujuan penggunaan profil, dan informasi kompetensi yang benar.

**Hasil yang akan diperoleh:** Draft presentasi tim yang siap diverifikasi.

### 76. RAB & Pricing Proposal
<!-- modal_id: rab_pricing_proposal -->
**Headline:** Penawaran harga yang transparan dan dapat dipertanggungjawabkan.

**Deskripsi:** Sajikan rincian biaya dan nilai penawaran dengan struktur yang mudah dipahami. Pastikan komponen harga sesuai perhitungan dan ketentuan yang berlaku.

**Yang bisa Anda lakukan:**
- Mengambil data dari costing.
- Menyusun rincian harga.
- Menampilkan total penawaran.
- Menambahkan asumsi dan ketentuan harga.

**Yang perlu disiapkan:** RAB, harga pemasok, jumlah peserta, dan kebijakan harga perusahaan.

**Hasil yang akan diperoleh:** Draft bagian biaya proposal yang konsisten dengan data perhitungan.

### 77. Portfolio Attachment
<!-- modal_id: portfolio_attachment -->
**Headline:** Perkuat proposal dengan bukti pengalaman yang relevan.

**Deskripsi:** Pilih pengalaman dan dokumentasi yang paling sesuai dengan kebutuhan klien agar proposal tidak hanya berisi janji, tetapi juga menunjukkan rekam jejak.

**Yang bisa Anda lakukan:**
- Memilih proyek relevan.
- Menambahkan foto dan ringkasan pekerjaan.
- Menyusun lampiran pengalaman.
- Mengatur urutan portofolio.

**Yang perlu disiapkan:** Data pengalaman dan bukti yang boleh digunakan.

**Hasil yang akan diperoleh:** Draft lampiran portofolio yang relevan dan dapat diverifikasi.

### 78. Legal Attachments
<!-- modal_id: legal_attachments -->
**Headline:** Lengkapi proposal dengan dokumen pendukung yang tepat.

**Deskripsi:** Pilih dokumen legalitas dan administrasi yang diminta oleh klien atau persyaratan pekerjaan. Kelengkapan harus mengikuti kebutuhan aktual, bukan sekadar menambahkan semua dokumen.

**Yang bisa Anda lakukan:**
- Memilih dokumen dari arsip perusahaan.
- Mengelompokkan lampiran.
- Memeriksa versi dan masa berlaku.
- Menyusun urutan lampiran.

**Yang perlu disiapkan:** Daftar persyaratan dan dokumen perusahaan yang valid.

**Hasil yang akan diperoleh:** Draft lampiran legal dan administrasi yang sesuai daftar kebutuhan.

### 79. Terms & Conditions
<!-- modal_id: terms_conditions -->
**Headline:** Perjelas kesepakatan sejak awal agar kerja sama lebih nyaman.

**Deskripsi:** Susun ketentuan layanan, pembayaran, perubahan jadwal, pembatalan, dan tanggung jawab pihak terkait secara jelas.

**Yang bisa Anda lakukan:**
- Menyusun ketentuan pembayaran.
- Menjelaskan perubahan dan pembatalan.
- Mencantumkan batasan layanan.
- Menyiapkan bagian persetujuan.

**Yang perlu disiapkan:** Kebijakan perusahaan, ruang lingkup layanan, dan ketentuan yang telah disepakati.

**Hasil yang akan diperoleh:** Draft syarat dan ketentuan untuk ditinjau sebelum disepakati. Untuk ketentuan hukum yang mengikat, lakukan pemeriksaan oleh pihak yang kompeten.

---

## H. Company & Business Data

### 80. Company Profile Data
<!-- modal_id: company_profile_data -->
**Headline:** Masukkan identitas perusahaan sekali, gunakan kembali di berbagai dokumen.

**Deskripsi:** Simpan informasi utama perusahaan sebagai sumber data bersama untuk quotation, invoice, proposal, surat, dan dokumen operasional.

**Yang bisa Anda lakukan:**
- Menyimpan nama dan identitas perusahaan.
- Mengatur alamat dan kontak.
- Menyimpan bidang usaha dan deskripsi layanan.
- Mengelola informasi yang tampil pada dokumen.

**Yang perlu disiapkan:** Data resmi dan informasi perusahaan yang telah diperiksa.

**Hasil yang akan diperoleh:** Profil perusahaan terpusat untuk digunakan kembali secara konsisten.

### 81. Brand Identity
<!-- modal_id: brand_identity -->
**Headline:** Jaga tampilan setiap dokumen tetap mencerminkan merek Anda.

**Deskripsi:** Atur elemen identitas visual agar dokumen dan komunikasi bisnis memiliki tampilan yang konsisten dan mudah dikenali.

**Yang bisa Anda lakukan:**
- Mengatur logo dan warna merek.
- Menentukan gaya visual dokumen.
- Mengelola elemen identitas perusahaan.
- Menggunakan identitas pada template.

**Yang perlu disiapkan:** Logo, warna, font, dan pedoman merek jika tersedia.

**Hasil yang akan diperoleh:** Pengaturan identitas visual yang dapat digunakan pada berbagai dokumen.

### 82. Company Contacts
<!-- modal_id: company_contacts -->
**Headline:** Informasi kontak resmi selalu siap digunakan.

**Deskripsi:** Kelola alamat, telepon, email, situs web, dan kontak resmi perusahaan agar tidak perlu dimasukkan berulang kali.

**Yang bisa Anda lakukan:**
- Menyimpan kontak utama dan cabang.
- Menentukan kontak yang tampil di dokumen.
- Memperbarui informasi komunikasi.
- Mengelola kontak penanggung jawab.

**Yang perlu disiapkan:** Informasi kontak resmi dan pihak yang bertanggung jawab.

**Hasil yang akan diperoleh:** Data kontak terpusat dan konsisten.

### 83. Bank Accounts
<!-- modal_id: bank_accounts -->
**Headline:** Informasi rekening pembayaran tersaji jelas dan terkontrol.

**Deskripsi:** Simpan rekening perusahaan yang digunakan untuk pembayaran pelanggan. Atur informasi yang boleh ditampilkan pada invoice atau dokumen pembayaran.

**Yang bisa Anda lakukan:**
- Menyimpan nama bank dan pemilik rekening.
- Mengelola beberapa rekening jika diperlukan.
- Menentukan rekening yang digunakan pada dokumen.
- Memperbarui informasi rekening.

**Yang perlu disiapkan:** Informasi rekening resmi milik perusahaan.

**Hasil yang akan diperoleh:** Data rekening yang konsisten pada dokumen pembayaran. Batasi akses hanya kepada pengguna berwenang.

### 84. Signatory Data
<!-- modal_id: signatory_data -->
**Headline:** Identitas penandatangan dokumen lebih tertata.

**Deskripsi:** Kelola nama, jabatan, dan informasi pejabat yang berwenang menandatangani dokumen perusahaan.

**Yang bisa Anda lakukan:**
- Menyimpan data penandatangan.
- Menentukan jabatan dan kapasitas.
- Memilih penandatangan sesuai jenis dokumen.
- Mengatur tampilan blok tanda tangan.

**Yang perlu disiapkan:** Data pejabat dan dasar kewenangan penandatangan.

**Hasil yang akan diperoleh:** Informasi penandatangan yang siap digunakan setelah diverifikasi.

### 85. Document Numbering
<!-- modal_id: document_numbering -->
**Headline:** Nomor dokumen lebih konsisten dan mudah dilacak.

**Deskripsi:** Atur pola penomoran untuk quotation, invoice, kuitansi, surat, dan dokumen lainnya sesuai kebijakan perusahaan.

**Yang bisa Anda lakukan:**
- Menentukan format nomor dokumen.
- Mengatur kode jenis dokumen.
- Mengelola periode atau urutan nomor.
- Mengurangi risiko nomor ganda.

**Yang perlu disiapkan:** Kebijakan penomoran dan format yang digunakan perusahaan.

**Hasil yang akan diperoleh:** Pola penomoran yang lebih tertib dan konsisten.

### 86. Customer Database
<!-- modal_id: customer_database -->
**Headline:** Kenali pelanggan dan riwayat kebutuhannya dengan lebih baik.

**Deskripsi:** Simpan informasi pelanggan dan riwayat interaksi agar tim dapat memberikan layanan yang lebih cepat dan relevan.

**Yang bisa Anda lakukan:**
- Menyimpan identitas dan kontak pelanggan.
- Mengelompokkan pelanggan.
- Melihat riwayat proyek dan penawaran.
- Menambahkan catatan kebutuhan.

**Yang perlu disiapkan:** Data pelanggan yang diperoleh secara sah dan sesuai tujuan penggunaan.

**Hasil yang akan diperoleh:** Database pelanggan yang lebih terorganisasi. Lindungi akses dan penggunaan data pribadi.

### 87. Supplier Database
<!-- modal_id: supplier_database -->
**Headline:** Temukan informasi pemasok tanpa harus mencari dari awal.

**Deskripsi:** Simpan data pemasok dan mitra layanan agar tim dapat membandingkan kebutuhan, meninjau riwayat, dan menghubungi pihak terkait.

**Yang bisa Anda lakukan:**
- Menyimpan profil dan kontak pemasok.
- Mengelompokkan jenis layanan.
- Mencatat harga dan tanggal pembaruan.
- Menyimpan catatan kerja sama.

**Yang perlu disiapkan:** Data pemasok, penawaran harga, dan informasi kerja sama.

**Hasil yang akan diperoleh:** Database pemasok yang lebih siap digunakan dalam perencanaan biaya.

### 88. Package & Product Database
<!-- modal_id: package_product_database -->
**Headline:** Semua paket dan layanan tersimpan sebagai katalog kerja.

**Deskripsi:** Bangun pusat data produk perjalanan yang dapat digunakan kembali dalam penawaran, costing, dan dokumen operasional.

**Yang bisa Anda lakukan:**
- Menyimpan nama dan deskripsi paket.
- Mengatur fasilitas dan ketentuan.
- Menyimpan komponen harga.
- Mengelompokkan produk berdasarkan jenis.

**Yang perlu disiapkan:** Informasi paket, layanan, fasilitas, dan harga terbaru.

**Hasil yang akan diperoleh:** Katalog produk yang konsisten dan lebih mudah diperbarui.

### 89. Destination Database
<!-- modal_id: destination_database -->
**Headline:** Bangun referensi destinasi untuk mempercepat penyusunan perjalanan.

**Deskripsi:** Simpan informasi destinasi, daya tarik, lokasi, fasilitas, dan catatan kunjungan untuk digunakan saat merancang paket.

**Yang bisa Anda lakukan:**
- Menyimpan profil destinasi.
- Mengelompokkan berdasarkan wilayah atau jenis.
- Mencatat fasilitas dan aktivitas.
- Menambahkan catatan operasional.

**Yang perlu disiapkan:** Informasi destinasi yang telah diperiksa dan diperbarui.

**Hasil yang akan diperoleh:** Referensi destinasi yang lebih mudah digunakan dalam perencanaan perjalanan.

### 90. Transport Database
<!-- modal_id: transport_database -->
**Headline:** Data armada dan layanan transportasi lebih mudah dikelola.

**Deskripsi:** Simpan informasi kendaraan, kapasitas, jenis layanan, dan pemasok transportasi untuk mendukung perencanaan perjalanan.

**Yang bisa Anda lakukan:**
- Mencatat jenis dan kapasitas kendaraan.
- Menyimpan kontak operator.
- Mencatat area layanan.
- Menyimpan harga berdasarkan tanggal pembaruan.

**Yang perlu disiapkan:** Data kendaraan dan informasi operator yang telah dikonfirmasi.

**Hasil yang akan diperoleh:** Referensi transportasi yang lebih tertata.

### 91. Hotel & Accommodation Database
<!-- modal_id: hotel_accommodation_database -->
**Headline:** Kelola referensi akomodasi untuk penawaran yang lebih cepat.

**Deskripsi:** Simpan data hotel, tipe kamar, fasilitas, kontak reservasi, dan informasi harga sebagai referensi saat menyusun paket.

**Yang bisa Anda lakukan:**
- Menyimpan profil akomodasi.
- Mencatat tipe kamar dan kapasitas.
- Menyimpan fasilitas dan kontak.
- Mencatat harga beserta tanggal pembaruan.

**Yang perlu disiapkan:** Informasi hotel dan harga yang dikonfirmasi kepada penyedia.

**Hasil yang akan diperoleh:** Database akomodasi yang siap menjadi referensi, bukan jaminan ketersediaan kamar.

### 92. Staff Database
<!-- modal_id: staff_database -->
**Headline:** Data tim tersusun agar penugasan lebih mudah.

**Deskripsi:** Simpan informasi staf dan kompetensi yang relevan untuk mendukung penugasan proyek dan kebutuhan dokumen perusahaan.

**Yang bisa Anda lakukan:**
- Menyimpan profil staf.
- Mencatat peran dan keahlian.
- Mengelola informasi kontak kerja.
- Menghubungkan staf dengan proyek.

**Yang perlu disiapkan:** Data staf dan persetujuan penggunaan informasi.

**Hasil yang akan diperoleh:** Database tim yang lebih terorganisasi dengan akses terbatas sesuai peran.

### 93. Partner Database
<!-- modal_id: partner_database -->
**Headline:** Bangun jaringan mitra yang mudah ditelusuri dan dikembangkan.

**Deskripsi:** Kelola informasi mitra strategis, komunitas, penyedia layanan, dan pihak pendukung lainnya dalam satu direktori.

**Yang bisa Anda lakukan:**
- Menyimpan profil mitra.
- Mencatat bentuk kerja sama.
- Menyimpan kontak dan catatan komunikasi.
- Mengelompokkan mitra berdasarkan bidang.

**Yang perlu disiapkan:** Data mitra dan informasi kerja sama yang telah dikonfirmasi.

**Hasil yang akan diperoleh:** Direktori mitra yang membantu pengembangan jaringan bisnis.

---

## I. Document Management

### 94. Document Archive
<!-- modal_id: document_archive -->
**Headline:** Semua dokumen bisnis lebih mudah ditemukan kembali.

**Deskripsi:** Simpan dan kelompokkan dokumen berdasarkan jenis, pelanggan, proyek, tanggal, atau status agar arsip tidak tercecer.

**Yang bisa Anda lakukan:**
- Mengarsipkan dokumen.
- Mencari berdasarkan kata kunci dan kategori.
- Menghubungkan dokumen dengan proyek.
- Melihat status dan tanggal dokumen.

**Yang perlu disiapkan:** Dokumen yang akan diarsipkan dan metadata pendukung.

**Hasil yang akan diperoleh:** Arsip digital yang lebih rapi dan mudah ditelusuri.

### 95. Document Search
<!-- modal_id: document_search -->
**Headline:** Temukan dokumen yang dibutuhkan tanpa membuka folder satu per satu.

**Deskripsi:** Cari dokumen berdasarkan nama, nomor, pelanggan, proyek, jenis, atau informasi lain yang tersimpan.

**Yang bisa Anda lakukan:**
- Mencari berdasarkan kata kunci.
- Memfilter jenis dan tanggal.
- Menelusuri dokumen terkait proyek.
- Membuka hasil pencarian yang relevan.

**Yang perlu disiapkan:** Dokumen yang sudah tersimpan dan memiliki informasi pencarian.

**Hasil yang akan diperoleh:** Proses pencarian dokumen yang lebih cepat.

### 96. Document Preview
<!-- modal_id: document_preview -->
**Headline:** Periksa isi dokumen sebelum dibagikan atau dicetak.

**Deskripsi:** Tinjau tampilan dan isi dokumen untuk memastikan informasi, susunan, serta identitas perusahaan sudah benar.

**Yang bisa Anda lakukan:**
- Melihat pratinjau dokumen.
- Memeriksa halaman dan tata letak.
- Meninjau informasi penting.
- Kembali melakukan revisi jika diperlukan.

**Yang perlu disiapkan:** Draft dokumen yang akan diperiksa.

**Hasil yang akan diperoleh:** Kesempatan memeriksa dokumen sebelum diterbitkan.

### 97. PDF Export
<!-- modal_id: pdf_export -->
**Headline:** Ubah dokumen menjadi PDF yang siap dibagikan.

**Deskripsi:** Siapkan dokumen dalam format PDF dengan tata letak yang lebih konsisten untuk kebutuhan pengiriman, arsip, atau pencetakan.

**Yang bisa Anda lakukan:**
- Mengekspor dokumen ke PDF.
- Memeriksa hasil halaman.
- Menggunakan identitas perusahaan.
- Menyiapkan file untuk dibagikan.

**Yang perlu disiapkan:** Dokumen yang telah selesai diperiksa.

**Hasil yang akan diperoleh:** File PDF final setelah pengguna menyetujui isi dan tampilannya.

### 98. Print Layout
<!-- modal_id: print_layout -->
**Headline:** Dokumen siap cetak dengan tata letak yang lebih rapi.

**Deskripsi:** Atur halaman agar informasi tidak terpotong dan tampil baik saat dicetak.

**Yang bisa Anda lakukan:**
- Meninjau ukuran kertas.
- Mengatur margin dan pemisahan halaman.
- Memeriksa header dan footer.
- Menyiapkan tampilan cetak.

**Yang perlu disiapkan:** Draft dokumen dan kebutuhan ukuran kertas.

**Hasil yang akan diperoleh:** Tata letak cetak yang siap diperiksa.

### 99. Revision & Version History
<!-- modal_id: revision_version_history -->
**Headline:** Setiap perubahan dokumen lebih mudah ditelusuri.

**Deskripsi:** Simpan riwayat versi agar tim mengetahui perubahan yang dilakukan dan dapat membandingkan draft sebelumnya.

**Yang bisa Anda lakukan:**
- Menyimpan versi dokumen.
- Mencatat waktu dan pengguna yang mengubah.
- Melihat riwayat revisi.
- Mengembalikan atau menyalin versi sebelumnya sesuai aturan sistem.

**Yang perlu disiapkan:** Dokumen yang dikelola dan aktivitas revisi.

**Hasil yang akan diperoleh:** Riwayat perubahan yang membantu menjaga kontrol dokumen.

### 100. Duplicate Document
<!-- modal_id: duplicate_document -->
**Headline:** Buat dokumen baru dari format yang sudah ada.

**Deskripsi:** Gunakan dokumen terdahulu sebagai dasar pekerjaan baru agar tidak perlu menyusun ulang seluruh format. Pastikan data lama diganti dan diperiksa.

**Yang bisa Anda lakukan:**
- Menyalin struktur dokumen.
- Mengganti data pelanggan dan proyek.
- Mempertahankan format yang diperlukan.
- Memeriksa informasi yang masih terbawa.

**Yang perlu disiapkan:** Dokumen acuan dan data pekerjaan baru.

**Hasil yang akan diperoleh:** Draft dokumen baru yang lebih cepat disiapkan.

### 101. Document Templates
<!-- modal_id: document_templates -->
**Headline:** Standarkan dokumen agar hasil kerja tim tetap konsisten.

**Deskripsi:** Kelola template resmi perusahaan untuk quotation, invoice, proposal, surat, dan dokumen operasional.

**Yang bisa Anda lakukan:**
- Memilih template berdasarkan jenis dokumen.
- Mengatur identitas dan susunan.
- Mengelola versi template.
- Menentukan template yang digunakan tim.

**Yang perlu disiapkan:** Format dokumen dan identitas visual perusahaan.

**Hasil yang akan diperoleh:** Template terpusat untuk menjaga konsistensi dokumen.

### 102. Branded Documents
<!-- modal_id: branded_documents -->
**Headline:** Setiap dokumen membawa citra profesional perusahaan.

**Deskripsi:** Terapkan identitas visual perusahaan secara konsisten pada dokumen yang dibuat, sehingga komunikasi bisnis terlihat lebih terpercaya.

**Yang bisa Anda lakukan:**
- Menggunakan logo dan warna perusahaan.
- Menampilkan header dan footer.
- Menyesuaikan elemen visual.
- Menggunakan format yang konsisten.

**Yang perlu disiapkan:** Identitas merek dan template dokumen.

**Hasil yang akan diperoleh:** Dokumen dengan tampilan yang lebih seragam dan profesional.

### 103. Approval Workflow
<!-- modal_id: approval_workflow -->
**Headline:** Dokumen penting melewati pemeriksaan sebelum diterbitkan.

**Deskripsi:** Atur alur pemeriksaan dan persetujuan agar dokumen tidak langsung digunakan tanpa otorisasi pihak yang tepat.

**Yang bisa Anda lakukan:**
- Menentukan pemeriksa dan pemberi persetujuan.
- Mengatur status draft, review, revisi, dan disetujui.
- Memberikan catatan koreksi.
- Melihat status persetujuan.

**Yang perlu disiapkan:** Struktur tim, peran, dan aturan persetujuan perusahaan.

**Hasil yang akan diperoleh:** Alur kontrol dokumen yang lebih jelas.

### 104. Document Sharing
<!-- modal_id: document_sharing -->
**Headline:** Bagikan dokumen dengan lebih terkontrol.

**Deskripsi:** Siapkan dokumen untuk dibagikan kepada pelanggan atau mitra dengan memperhatikan versi, penerima, dan hak akses.

**Yang bisa Anda lakukan:**
- Menyiapkan dokumen untuk dibagikan.
- Memilih versi yang tepat.
- Mengatur akses sesuai kemampuan sistem.
- Mencatat referensi pembagian dokumen.

**Yang perlu disiapkan:** Dokumen yang telah disetujui dan data penerima.

**Hasil yang akan diperoleh:** Proses berbagi dokumen yang lebih tertib dan memperhatikan kerahasiaan.

---

## J. Communication & Customer Service

### 105. WhatsApp Message Generator
<!-- modal_id: whatsapp_message_generator -->
**Headline:** Balas pelanggan lebih cepat tanpa kehilangan sentuhan personal.

**Deskripsi:** Siapkan pesan WhatsApp untuk berbagai kebutuhan bisnis travel. Pilih situasi komunikasi, masukkan informasi penting, lalu dapatkan draft pesan yang siap disesuaikan.

**Yang bisa Anda lakukan:**
- Membuat balasan inquiry.
- Mengirim pengantar penawaran.
- Menyampaikan konfirmasi booking.
- Menyiapkan follow-up dan ucapan terima kasih.

**Yang perlu disiapkan:** Konteks percakapan, nama pelanggan, dan informasi layanan.

**Hasil yang akan diperoleh:** Draft pesan WhatsApp yang praktis dan profesional. Pada tahap awal, pesan disalin dan dikirim oleh pengguna.

### 106. Inquiry Response
<!-- modal_id: inquiry_response -->
**Headline:** Ubah pertanyaan calon pelanggan menjadi peluang penjualan.

**Deskripsi:** Siapkan jawaban yang cepat, informatif, dan sesuai kebutuhan pelanggan. Bantu tim merespons pertanyaan tanpa harus merangkai jawaban dari awal.

**Yang bisa Anda lakukan:**
- Menjawab pertanyaan paket dan layanan.
- Menjelaskan fasilitas dan ketentuan.
- Menyusun pertanyaan klarifikasi.
- Mengarahkan pelanggan ke langkah berikutnya.

**Yang perlu disiapkan:** Pertanyaan pelanggan dan informasi produk yang benar.

**Hasil yang akan diperoleh:** Draft jawaban inquiry yang siap diperiksa dan dikirim.

### 107. Quotation Delivery Message
<!-- modal_id: quotation_delivery_message -->
**Headline:** Kirim penawaran dengan pesan pengantar yang membuat pelanggan nyaman meninjau.

**Deskripsi:** Siapkan pesan singkat saat mengirim quotation atau proposal. Sampaikan konteks, ringkasan, dan ajakan untuk berdiskusi secara profesional.

**Yang bisa Anda lakukan:**
- Membuat pesan pengantar penawaran.
- Menyebutkan dokumen yang dilampirkan.
- Mengajak pelanggan memberi tanggapan.
- Menyesuaikan gaya komunikasi.

**Yang perlu disiapkan:** Nama pelanggan, nomor atau judul penawaran, dan ringkasan layanan.

**Hasil yang akan diperoleh:** Draft pesan pengiriman penawaran yang siap digunakan.

### 108. Booking Confirmation Message
<!-- modal_id: booking_confirmation_message -->
**Headline:** Konfirmasi pemesanan dengan informasi yang jelas dan menenangkan.

**Deskripsi:** Siapkan pesan setelah pemesanan disepakati agar pelanggan mengetahui ringkasan layanan dan langkah berikutnya.

**Yang bisa Anda lakukan:**
- Menyampaikan ringkasan booking.
- Menginformasikan jadwal dan kebutuhan data.
- Menyampaikan status pembayaran sesuai catatan.
- Memberikan informasi kontak bantuan.

**Yang perlu disiapkan:** Data booking yang telah dikonfirmasi.

**Hasil yang akan diperoleh:** Draft pesan konfirmasi yang siap diperiksa.

### 109. Payment Reminder Message
<!-- modal_id: payment_reminder_message -->
**Headline:** Pengingat pembayaran yang sopan, jelas, dan tidak canggung.

**Deskripsi:** Susun pesan pengingat sesuai status tagihan dan hubungan dengan pelanggan. Sampaikan nominal serta jatuh tempo berdasarkan data yang benar.

**Yang bisa Anda lakukan:**
- Membuat pengingat sebelum jatuh tempo.
- Menyusun pengingat pelunasan.
- Menyesuaikan nada komunikasi.
- Mencantumkan referensi invoice.

**Yang perlu disiapkan:** Data invoice, nominal, jatuh tempo, dan status pembayaran.

**Hasil yang akan diperoleh:** Draft pesan pengingat pembayaran yang siap dikirim.

### 110. Travel Reminder Message
<!-- modal_id: travel_reminder_message -->
**Headline:** Bantu pelanggan lebih siap sebelum hari keberangkatan.

**Deskripsi:** Kirim informasi pengingat terkait jadwal, titik kumpul, perlengkapan, dan hal penting lainnya agar peserta tidak melewatkan persiapan.

**Yang bisa Anda lakukan:**
- Menyusun pengingat H-7, H-3, atau H-1.
- Menyampaikan titik kumpul dan waktu.
- Membuat daftar perlengkapan.
- Mengingatkan ketentuan perjalanan.

**Yang perlu disiapkan:** Jadwal, itinerary, titik kumpul, dan informasi persiapan.

**Hasil yang akan diperoleh:** Draft pesan pengingat perjalanan yang sesuai jadwal.

### 111. Customer Follow-up
<!-- modal_id: customer_follow_up -->
**Headline:** Bangun hubungan jangka panjang, bukan hanya transaksi sekali jalan.

**Deskripsi:** Siapkan tindak lanjut setelah penawaran, perjalanan, atau interaksi pelanggan. Komunikasi yang tepat dapat membuka peluang repeat order dan rekomendasi.

**Yang bisa Anda lakukan:**
- Menyusun pesan setelah penawaran.
- Menanyakan pengalaman pelanggan.
- Menawarkan layanan lanjutan yang relevan.
- Menjaga hubungan dengan pelanggan lama.

**Yang perlu disiapkan:** Riwayat interaksi dan tujuan follow-up.

**Hasil yang akan diperoleh:** Draft pesan tindak lanjut yang lebih personal dan terarah.

### 112. Thank-you Message
<!-- modal_id: thank_you_message -->
**Headline:** Akhiri layanan dengan kesan baik yang ingin diingat pelanggan.

**Deskripsi:** Siapkan ucapan terima kasih setelah perjalanan atau layanan selesai. Sampaikan apresiasi dengan bahasa yang hangat dan profesional.

**Yang bisa Anda lakukan:**
- Membuat ucapan terima kasih.
- Menyesuaikan pesan dengan jenis layanan.
- Menyampaikan kontak bantuan.
- Mengundang pelanggan untuk kembali.

**Yang perlu disiapkan:** Nama pelanggan dan jenis layanan yang telah diterima.

**Hasil yang akan diperoleh:** Draft pesan apresiasi yang siap dikirim.

### 113. Feedback Request
<!-- modal_id: feedback_request -->
**Headline:** Dengarkan pelanggan untuk meningkatkan kualitas layanan.

**Deskripsi:** Minta masukan pelanggan melalui pertanyaan yang sederhana dan relevan. Gunakan hasilnya sebagai bahan evaluasi pelayanan.

**Yang bisa Anda lakukan:**
- Menyusun pesan permintaan ulasan.
- Membuat pertanyaan evaluasi.
- Meminta masukan tentang layanan tertentu.
- Menyiapkan ucapan terima kasih atas tanggapan.

**Yang perlu disiapkan:** Jenis layanan dan aspek yang ingin dievaluasi.

**Hasil yang akan diperoleh:** Draft permintaan feedback yang siap dibagikan.

### 114. Complaint Response
<!-- modal_id: complaint_response -->
**Headline:** Hadapi keluhan dengan tenang, empati, dan langkah tindak lanjut yang jelas.

**Deskripsi:** Bantu tim menyusun respons awal terhadap keluhan pelanggan. Gunakan bahasa yang tidak defensif, akui pengalaman pelanggan, dan arahkan pada pemeriksaan fakta serta solusi.

**Yang bisa Anda lakukan:**
- Menyusun respons awal yang empatik.
- Merangkum inti keluhan.
- Menyiapkan pertanyaan klarifikasi.
- Menyusun langkah tindak lanjut.

**Yang perlu disiapkan:** Isi keluhan, kronologi, fakta yang telah diperiksa, dan kebijakan layanan.

**Hasil yang akan diperoleh:** Draft respons yang lebih terarah. Keputusan kompensasi atau penyelesaian tetap berada pada pihak berwenang.

---

## K. Business Reports & Analytics

### 115. Transaction Report
<!-- modal_id: transaction_report -->
**Headline:** Lihat pergerakan transaksi bisnis dalam laporan yang mudah dibaca.

**Deskripsi:** Rangkum transaksi berdasarkan periode, pelanggan, proyek, atau status agar kondisi usaha lebih mudah dipantau.

**Yang bisa Anda lakukan:**
- Melihat ringkasan transaksi.
- Memfilter periode dan status.
- Mengelompokkan berdasarkan proyek atau pelanggan.
- Menyiapkan laporan untuk evaluasi.

**Yang perlu disiapkan:** Data transaksi yang tercatat dan telah diperiksa.

**Hasil yang akan diperoleh:** Laporan transaksi berdasarkan data sistem.

### 116. Sales Report
<!-- modal_id: sales_report -->
**Headline:** Ketahui perkembangan penjualan dan sumber peluang bisnis.

**Deskripsi:** Tinjau penawaran, konversi, dan nilai penjualan untuk memahami aktivitas tim dan arah pertumbuhan usaha.

**Yang bisa Anda lakukan:**
- Melihat jumlah dan nilai penawaran.
- Memantau status prospek dan transaksi.
- Membandingkan periode penjualan.
- Mengidentifikasi layanan yang diminati.

**Yang perlu disiapkan:** Data pelanggan, penawaran, dan transaksi.

**Hasil yang akan diperoleh:** Ringkasan penjualan untuk membantu evaluasi strategi.

### 117. Customer Report
<!-- modal_id: customer_report -->
**Headline:** Pahami pelanggan yang paling aktif dan kebutuhan yang paling sering muncul.

**Deskripsi:** Lihat pola transaksi dan interaksi pelanggan agar perusahaan dapat merencanakan pelayanan dan penawaran yang lebih relevan.

**Yang bisa Anda lakukan:**
- Melihat pelanggan berdasarkan aktivitas.
- Meninjau riwayat transaksi.
- Mengelompokkan pelanggan.
- Mengidentifikasi peluang tindak lanjut.

**Yang perlu disiapkan:** Database pelanggan dan riwayat interaksi yang sah digunakan.

**Hasil yang akan diperoleh:** Ringkasan pelanggan untuk mendukung pengelolaan hubungan pelanggan.

### 118. Trip Report
<!-- modal_id: trip_report -->
**Headline:** Pantau pelaksanaan perjalanan dari rencana hingga realisasi.

**Deskripsi:** Rangkum jumlah perjalanan, status pelaksanaan, peserta, dan catatan operasional agar tim memahami aktivitas perjalanan perusahaan.

**Yang bisa Anda lakukan:**
- Melihat daftar perjalanan.
- Memfilter jadwal dan status.
- Meninjau jumlah peserta.
- Mengakses catatan penyelesaian.

**Yang perlu disiapkan:** Data proyek dan perjalanan yang tercatat.

**Hasil yang akan diperoleh:** Laporan operasional perjalanan berdasarkan data aktual.

### 119. Payment Report
<!-- modal_id: payment_report -->
**Headline:** Ketahui pembayaran yang sudah diterima dan yang masih menunggu.

**Deskripsi:** Pantau arus pembayaran berdasarkan invoice, pelanggan, dan proyek agar tindak lanjut keuangan lebih terarah.

**Yang bisa Anda lakukan:**
- Melihat pembayaran masuk.
- Memfilter status pembayaran.
- Meninjau tagihan yang belum lunas.
- Membandingkan pembayaran berdasarkan periode.

**Yang perlu disiapkan:** Invoice dan catatan pembayaran yang telah diverifikasi.

**Hasil yang akan diperoleh:** Ringkasan pembayaran yang dapat digunakan untuk pemantauan keuangan.

### 120. Receivables Report
<!-- modal_id: receivables_report -->
**Headline:** Kendalikan piutang sebelum mengganggu arus kas usaha.

**Deskripsi:** Lihat daftar tagihan yang belum lunas, nilai piutang, dan umur tagihan untuk membantu menentukan prioritas penagihan.

**Yang bisa Anda lakukan:**
- Melihat tagihan terbuka.
- Mengelompokkan berdasarkan jatuh tempo.
- Meninjau umur piutang.
- Menyiapkan daftar tindak lanjut.

**Yang perlu disiapkan:** Data invoice, jatuh tempo, dan pembayaran yang sudah diverifikasi.

**Hasil yang akan diperoleh:** Laporan piutang yang lebih mudah dipantau.

### 121. Trip Cost Report
<!-- modal_id: trip_cost_report -->
**Headline:** Pahami biaya aktual setiap perjalanan.

**Deskripsi:** Bandingkan biaya yang direncanakan dengan pengeluaran yang benar-benar terjadi. Temukan komponen yang perlu dikendalikan pada pekerjaan berikutnya.

**Yang bisa Anda lakukan:**
- Merangkum biaya per proyek.
- Mengelompokkan biaya berdasarkan kategori.
- Membandingkan rencana dan realisasi.
- Meninjau selisih biaya.

**Yang perlu disiapkan:** RAB dan catatan pengeluaran aktual.

**Hasil yang akan diperoleh:** Laporan biaya perjalanan yang membantu evaluasi efisiensi.

### 122. Project Profit Report
<!-- modal_id: project_profit_report -->
**Headline:** Ukur hasil setiap proyek untuk menentukan langkah bisnis berikutnya.

**Deskripsi:** Tinjau pendapatan, biaya, dan hasil akhir proyek secara lebih menyeluruh. Gunakan data untuk mengevaluasi harga dan pola layanan.

**Yang bisa Anda lakukan:**
- Melihat hasil finansial per proyek.
- Membandingkan proyek.
- Meninjau margin berdasarkan data.
- Mengidentifikasi faktor yang memengaruhi hasil.

**Yang perlu disiapkan:** Data pendapatan dan biaya yang lengkap.

**Hasil yang akan diperoleh:** Laporan profitabilitas proyek yang dapat menjadi dasar evaluasi.

### 123. Supplier Report
<!-- modal_id: supplier_report -->
**Headline:** Evaluasi pemasok berdasarkan data kerja sama.

**Deskripsi:** Tinjau penggunaan pemasok, nilai transaksi, dan catatan layanan untuk membantu perusahaan mengelola hubungan dengan mitra.

**Yang bisa Anda lakukan:**
- Melihat transaksi per pemasok.
- Meninjau riwayat penggunaan.
- Membandingkan harga yang tercatat.
- Menambahkan catatan evaluasi.

**Yang perlu disiapkan:** Database pemasok dan catatan transaksi.

**Hasil yang akan diperoleh:** Ringkasan pemasok untuk membantu evaluasi kerja sama. Perbandingan harga harus memperhatikan tanggal dan kesetaraan layanan.

### 124. Sales Performance Report
<!-- modal_id: sales_performance_report -->
**Headline:** Lihat aktivitas penjualan tim dengan ukuran yang lebih jelas.

**Deskripsi:** Pantau aktivitas dan hasil penjualan berdasarkan data yang tercatat agar evaluasi tim lebih objektif.

**Yang bisa Anda lakukan:**
- Melihat penawaran per anggota tim.
- Meninjau status prospek.
- Membandingkan hasil berdasarkan periode.
- Mengidentifikasi kebutuhan dukungan tim.

**Yang perlu disiapkan:** Data pengguna, aktivitas penjualan, dan transaksi.

**Hasil yang akan diperoleh:** Ringkasan kinerja penjualan berdasarkan indikator yang disepakati.

### 125. Operations Report
<!-- modal_id: operations_report -->
**Headline:** Ketahui kondisi operasional dan pekerjaan yang membutuhkan perhatian.

**Deskripsi:** Rangkum status perjalanan, kesiapan dokumen, penugasan tim, dan pekerjaan yang belum selesai agar koordinasi lebih mudah.

**Yang bisa Anda lakukan:**
- Melihat proyek berdasarkan status.
- Memantau kesiapan operasional.
- Meninjau penugasan tim.
- Mengidentifikasi pekerjaan tertunda.

**Yang perlu disiapkan:** Data proyek, jadwal, dokumen, dan penugasan.

**Hasil yang akan diperoleh:** Ringkasan operasional untuk membantu pengendalian pekerjaan.

### 126. Budget vs Actual Report
<!-- modal_id: budget_vs_actual_report -->
**Headline:** Bandingkan rencana anggaran dengan kenyataan di lapangan.

**Deskripsi:** Ketahui selisih antara biaya yang direncanakan dan pengeluaran aktual. Informasi ini membantu perusahaan memperbaiki estimasi dan pengendalian biaya.

**Yang bisa Anda lakukan:**
- Membandingkan anggaran dan realisasi.
- Melihat selisih per kategori.
- Menandai komponen yang melampaui anggaran.
- Menyusun catatan evaluasi.

**Yang perlu disiapkan:** RAB awal dan catatan biaya aktual.

**Hasil yang akan diperoleh:** Laporan perbandingan anggaran dan realisasi berdasarkan data yang tersedia.

---

## L. Settings & Access

### 127. Language Settings
<!-- modal_id: language_settings -->
**Headline:** Gunakan sistem dalam bahasa yang paling nyaman bagi tim.

**Deskripsi:** Atur bahasa antarmuka agar pengguna dapat bekerja dengan lebih mudah. Konten dokumen tetap mengikuti bahasa yang dipilih saat penyusunan.

**Yang bisa Anda lakukan:**
- Memilih bahasa antarmuka yang tersedia.
- Mengatur preferensi bahasa.
- Menggunakan format bahasa sesuai kebutuhan.

**Yang perlu disiapkan:** Preferensi bahasa pengguna.

**Hasil yang akan diperoleh:** Pengalaman penggunaan yang lebih sesuai dengan preferensi tim.

### 128. User Management
<!-- modal_id: user_management -->
**Headline:** Kelola siapa saja yang dapat menggunakan sistem perusahaan.

**Deskripsi:** Atur akun pengguna sesuai kebutuhan organisasi agar pekerjaan dapat dibagi dengan lebih tertib.

**Yang bisa Anda lakukan:**
- Menambahkan atau menonaktifkan pengguna.
- Mengelola informasi akun.
- Mengatur peran pengguna.
- Meninjau status akses.

**Yang perlu disiapkan:** Data pengguna dan kebijakan akses perusahaan.

**Hasil yang akan diperoleh:** Pengelolaan pengguna yang lebih terkontrol.

### 129. Roles & Permissions
<!-- modal_id: roles_permissions -->
**Headline:** Setiap anggota tim mendapat akses sesuai tanggung jawabnya.

**Deskripsi:** Tidak semua pengguna perlu melihat atau mengubah seluruh data. Atur hak akses agar informasi penting lebih terlindungi dan pekerjaan lebih terarah.

**Yang bisa Anda lakukan:**
- Menentukan peran admin, manajer, dan staf.
- Mengatur akses baca, buat, ubah, atau persetujuan.
- Membatasi akses dokumen sensitif.
- Meninjau hak akses pengguna.

**Yang perlu disiapkan:** Struktur organisasi dan kebijakan akses.

**Hasil yang akan diperoleh:** Pengaturan akses yang lebih sesuai dengan tanggung jawab masing-masing.

### 130. Approval Settings
<!-- modal_id: approval_settings -->
**Headline:** Tentukan siapa yang berhak memeriksa dan menyetujui pekerjaan.

**Deskripsi:** Atur alur persetujuan untuk dokumen atau transaksi penting agar proses kerja mengikuti kebijakan perusahaan.

**Yang bisa Anda lakukan:**
- Menentukan pihak pemeriksa.
- Mengatur tahap persetujuan.
- Menentukan dokumen yang memerlukan persetujuan.
- Mengelola aturan revisi.

**Yang perlu disiapkan:** Struktur kewenangan dan prosedur internal.

**Hasil yang akan diperoleh:** Pengaturan persetujuan yang lebih konsisten.

### 131. Template Settings
<!-- modal_id: template_settings -->
**Headline:** Atur standar dokumen perusahaan dari satu tempat.

**Deskripsi:** Kelola template yang digunakan oleh tim agar tampilan dan susunan dokumen tetap konsisten.

**Yang bisa Anda lakukan:**
- Menentukan template utama.
- Mengatur template berdasarkan jenis dokumen.
- Memperbarui versi template.
- Mengatur akses pengelolaan template.

**Yang perlu disiapkan:** Template dan standar dokumen perusahaan.

**Hasil yang akan diperoleh:** Pengelolaan template yang lebih terpusat.

### 132. Company Settings
<!-- modal_id: company_settings -->
**Headline:** Sesuaikan sistem dengan cara kerja perusahaan Anda.

**Deskripsi:** Kelola pengaturan umum seperti identitas, format, preferensi, dan aturan dasar yang digunakan dalam aktivitas bisnis.

**Yang bisa Anda lakukan:**
- Mengatur identitas perusahaan.
- Menentukan preferensi dokumen.
- Mengelola format tanggal dan angka.
- Mengatur konfigurasi dasar perusahaan.

**Yang perlu disiapkan:** Kebijakan dan informasi resmi perusahaan.

**Hasil yang akan diperoleh:** Pengaturan sistem yang lebih sesuai dengan kebutuhan usaha.

### 133. Backup & Export
<!-- modal_id: backup_export -->
**Headline:** Siapkan salinan data untuk mendukung pengelolaan informasi bisnis.

**Deskripsi:** Kelola pencadangan dan ekspor data sesuai kemampuan sistem dan hak akses pengguna. Data bisnis penting perlu memiliki prosedur perlindungan yang jelas.

**Yang bisa Anda lakukan:**
- Meninjau opsi pencadangan yang tersedia.
- Mengekspor data sesuai izin.
- Menyiapkan arsip untuk kebutuhan administrasi.
- Memeriksa waktu pencadangan terakhir jika tersedia.

**Yang perlu disiapkan:** Hak akses dan kebijakan pencadangan perusahaan.

**Hasil yang akan diperoleh:** Proses pengelolaan salinan data yang lebih terencana. Ketersediaan fitur backup mengikuti implementasi teknis.

### 134. Activity Log
<!-- modal_id: activity_log -->
**Headline:** Ketahui aktivitas penting yang terjadi di dalam sistem.

**Deskripsi:** Catat aktivitas pengguna dan perubahan penting agar pengelola dapat menelusuri riwayat pekerjaan serta membantu pemeriksaan jika terjadi masalah.

**Yang bisa Anda lakukan:**
- Melihat aktivitas pengguna.
- Menelusuri perubahan data.
- Memeriksa waktu aktivitas.
- Memfilter riwayat berdasarkan pengguna atau jenis tindakan.

**Yang perlu disiapkan:** Pengaturan pencatatan aktivitas dan hak akses administrator.

**Hasil yang akan diperoleh:** Jejak aktivitas yang mendukung transparansi dan pengawasan sistem.

### 135. Security Settings
<!-- modal_id: security_settings -->
**Headline:** Lindungi data bisnis dengan pengaturan akses yang tepat.

**Deskripsi:** Kelola pengaturan keamanan akun dan akses agar informasi perusahaan, pelanggan, transaksi, dan dokumen sensitif tidak terbuka kepada pihak yang tidak berwenang.

**Yang bisa Anda lakukan:**
- Mengatur kebijakan akses.
- Meninjau sesi dan akun pengguna jika tersedia.
- Mengelola pengamanan akun.
- Menetapkan kebijakan pengelolaan data.

**Yang perlu disiapkan:** Kebijakan keamanan dan administrator yang bertanggung jawab.

**Hasil yang akan diperoleh:** Pengelolaan keamanan yang lebih terarah sesuai fitur yang diterapkan.

---

# 3. Catatan penting untuk tim pengembangan

## A. Konsistensi pengalaman modal
- Semua kartu fitur membuka modal informasi, bukan langsung membuka form.
- Gunakan struktur konten yang sama agar pengguna cepat memahami pola interaksi.
- Judul, headline, dan deskripsi harus terlihat lebih dahulu.
- Bagian kemampuan, kebutuhan input, dan hasil dapat menggunakan daftar ringkas.
- Modal harus nyaman dibaca di layar ponsel dan dapat di-scroll jika kontennya panjang.
- Tombol aksi diletakkan di bagian bawah modal, dua kolom dengan lebar seimbang.

## B. Status tombol versi awal
- **Tutup:** aktif.
- **Buat:** nonaktif / disabled.
- Tombol nonaktif tetap terlihat jelas sebagai fitur yang disiapkan, tetapi jangan dibuat seolah-olah dapat digunakan.
- Jangan menghubungkan tombol Buat ke halaman kosong atau proses palsu.
- Saat fitur sudah selesai dikembangkan dan diuji, aktifkan tombol Buat hanya untuk fitur tersebut.

## C. Penanda fitur
Jika fitur belum tersedia, gunakan label **Segera Hadir** pada kartu atau di dalam modal. Jangan menyatakan fitur sudah berjalan apabila implementasinya belum tersedia.

## D. Prinsip kejujuran dan keamanan
- AI membantu membaca, merangkum, menyusun, dan memberi saran; pengguna tetap memeriksa hasil.
- Harga pemasok, ketersediaan hotel/kendaraan, pembayaran, legalitas, sertifikat, pengalaman, dan referensi tidak boleh dibuat-buat.
- Perhitungan biaya dan harga harus dilakukan dengan logika aplikasi yang dapat ditelusuri.
- Data pembayaran yang dimasukkan pengguna tidak otomatis dianggap telah terverifikasi.
- Dokumen legal dan tender harus mengikuti persyaratan aktual.
- Data pribadi pelanggan, peserta, staf, dan dokumen perusahaan harus dilindungi dengan hak akses yang sesuai.
- Dokumen final memerlukan pemeriksaan dan persetujuan manusia.

## E. Rekomendasi pemasangan
Konten ini dapat disimpan sebagai satu library konten modal. Saat pengembangan, setiap kartu cukup memanggil konten berdasarkan ID fitur, misalnya:
- `quotation_generator`
- `rab_costing`
- `travel_itinerary`
- `tender_checklist`
- `whatsapp_message_generator`

Dengan pendekatan ini, teks modal dapat diperbarui tanpa harus mengubah struktur komponen kartu satu per satu.

---

**Prinsip produk:** Satu kali memasukkan data, banyak pekerjaan dan dokumen bisa disiapkan. AI membantu mempercepat pekerjaan; sistem menjaga perhitungan dan struktur; manusia tetap memeriksa dan menyetujui hasil akhir.
