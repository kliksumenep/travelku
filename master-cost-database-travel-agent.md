# MASTER COST DATABASE TRAVEL AGENT
## Daftar induk belanja, biaya, dan pengeluaran perjalanan — Draft fondasi sistem

**Versi:** 1.0  
**Tujuan:** Menjadi sumber data induk untuk membuat daftar kebutuhan biaya secara otomatis, menyusun anggaran/RAB, menghitung HPP dan harga jual, mengendalikan pengeluaran aktual, serta mengevaluasi hasil proyek travel agent.

---

## 1. Prinsip desain

1. **Satu master database untuk semua skala.** Simple, Professional, dan Enterprise memakai sumber data yang sama. Perbedaan skala hanya menentukan komponen mana yang ditampilkan secara default dan seberapa dalam kontrolnya.
2. **Sepuluh master kategori untuk tampilan utama.** Kategori dibuat ringkas agar travel agent kecil tidak kewalahan. Rincian item tetap lengkap di bawahnya.
3. **Jenis perjalanan adalah filter terpisah.** Domestic, inbound, outbound, corporate/MICE, educational tour, event/gathering, dan jenis lain tidak dibuat sebagai master kategori baru.
4. **Daftar proyek dibuat otomatis.** Sistem memilih item berdasarkan jenis perjalanan, itinerary, durasi, jumlah peserta, fasilitas, moda transportasi, negara tujuan, dan profil proyek.
5. **Tidak semua item harus digunakan.** Item yang tidak relevan dapat dikeluarkan dari proyek, tetapi tidak menghapus item dari master database.
6. **Harga tidak boleh dianggap selalu tersedia atau selalu benar.** Setiap harga harus memiliki sumber, tanggal, masa berlaku, status verifikasi, dan mata uang.
7. **Pisahkan rencana, komitmen, dan realisasi.** Anggaran, pesanan/kontrak vendor, tagihan, dan pembayaran adalah keadaan yang berbeda.
8. **Hindari biaya ganda.** Sistem perlu mencatat apakah harga paket vendor sudah termasuk driver, BBM, pajak, service charge, parkir, atau komponen lain.
9. **AI membantu menemukan kebutuhan; mesin hitung menghitung angka.** AI boleh membaca itinerary dan menyarankan item, tetapi perhitungan total, pajak, margin, saldo, dan validasi dilakukan oleh aturan/kode yang teruji.
10. **Kelengkapan bukan berarti semua item wajib dibeli.** Sistem mengingatkan, meminta konfirmasi, dan menyimpan alasan item tidak digunakan.

---

## 2. Sepuluh master kategori

Sepuluh kategori berikut menjadi navigasi utama pada halaman costing. Kategori lama yang terlalu spesifik digabung agar tampilan sederhana, tetapi rincian tetap tersedia.

| Kode | Master kategori | Cakupan yang digabung | Contoh |
|---|---|---|---|
| MC01 | Transportasi & Mobilitas | Transportasi darat, udara, laut, kereta, transfer, biaya kendaraan | Bus, mobil, BBM, tol, parkir, tiket pesawat, bagasi |
| MC02 | Akomodasi | Hotel dan tempat menginap peserta maupun kru | Hotel, villa, homestay, extra bed, kamar kru |
| MC03 | Konsumsi & Hospitality | Makan, minum, snack, jamuan, kebutuhan diet | Breakfast, lunch, dinner, coffee break, air mineral |
| MC04 | Tiket Wisata & Aktivitas | Tiket masuk, wahana, atraksi, pengalaman, aktivitas | Tiket destinasi, perahu, outbound, instruktur aktivitas |
| MC05 | SDM, Guide & Tenaga Pelaksana | Honor, upah, uang harian, tenaga ahli dan kru | Tour leader, guide, interpreter, fasilitator, tenaga medis |
| MC06 | Perlengkapan, P3K & Kebutuhan Peserta | Barang habis pakai, perlengkapan reusable, logistik peserta dan keselamatan | Antimo, Betadine, plester, kantong muntah, tisu, name tag |
| MC07 | Produksi Acara, Dokumentasi & Peralatan Teknis | Kebutuhan event/MICE, produksi, dokumentasi, alat teknis | Venue, panggung, sound, LED, backdrop, foto/video |
| MC08 | Administrasi, Komunikasi & Perizinan | Administrasi proyek, komunikasi, dokumen, koordinasi, perizinan | ATK, cetak, internet, pulsa, izin kegiatan, survey |
| MC09 | Keuangan, Komisi & Pajak | Biaya transaksi, biaya pendanaan, komisi, pungutan/pajak terkait | Transfer, payment gateway, komisi agen, pajak transaksi |
| MC10 | Overhead, Risiko & Cadangan Proyek | Alokasi biaya perusahaan dan biaya ketidakpastian proyek | Alokasi kantor, software, penyusutan, contingency, pembatalan |

**Catatan implementasi:** MC10 bukan tempat untuk memasukkan semua biaya yang tidak diketahui kategorinya. Item harus tetap memiliki nama dan dasar perhitungan yang jelas. Biaya overhead perusahaan dan cadangan risiko juga harus dibedakan secara internal melalui subkategori dan tipe biaya.

---

## 3. Klasifikasi biaya — edukasi yang tertanam di sistem

Klasifikasi ini penting untuk mengajari pengguna tanpa membuat mereka harus memahami akuntansi terlebih dahulu. Saat pengguna menambah atau membuka item, tampilkan label sederhana dan ikon bantuan `?` yang menjelaskan artinya.

### 3.1 Berdasarkan hubungan dengan proyek

| Kode | Klasifikasi | Penjelasan sederhana | Contoh |
|---|---|---|---|
| COST-DIR | Biaya langsung | Dapat ditelusuri langsung ke proyek/tour tertentu | Bus untuk Tour A, hotel peserta Tour A |
| COST-IND | Biaya tidak langsung | Mendukung pekerjaan/perusahaan dan perlu dialokasikan secara wajar | Gaji admin, internet kantor, software |
| COST-MIX | Biaya campuran | Sebagian tetap dan sebagian berubah mengikuti pemakaian | Telepon/internet, kendaraan operasional |

**Aturan:** biaya langsung masuk ke anggaran proyek. Biaya tidak langsung dapat dialokasikan ke proyek melalui metode yang ditetapkan perusahaan. Jangan otomatis membebankan seluruh biaya kantor ke satu tour.

### 3.2 Berdasarkan perilaku terhadap jumlah peserta/aktivitas

| Kode | Klasifikasi | Penjelasan | Contoh |
|---|---|---|---|
| BEH-FIX | Tetap | Tidak berubah dalam rentang kapasitas tertentu | Sewa bus per hari, honor tetap tour leader |
| BEH-VAR | Variabel | Berubah mengikuti jumlah peserta atau pemakaian | Makan per pax, tiket per orang |
| BEH-STEP | Bertingkat | Berubah ketika melewati batas kapasitas | Tambah bus saat peserta melewati kapasitas |
| BEH-MIX | Campuran | Memiliki bagian tetap dan variabel | Paket venue dengan konsumsi per peserta |

### 3.3 Berdasarkan kewajiban/pemakaian dalam proyek

| Kode | Klasifikasi | Penjelasan | Contoh |
|---|---|---|---|
| USE-REQ | Wajib | Harus tersedia sesuai kontrak, keselamatan, atau desain paket | Kendaraan yang dijanjikan, tiket yang termasuk paket |
| USE-REC | Direkomendasikan | Sangat disarankan untuk kelancaran/kenyamanan; perlu keputusan pengguna | P3K dasar, kantong muntah, air mineral cadangan |
| USE-CND | Kondisional | Hanya muncul jika kondisi tertentu terjadi | Overtime, extra bed, visa bila diperlukan |
| USE-OPT | Opsional | Tambahan berdasarkan permintaan/persetujuan klien | Dokumentasi premium, upgrade, merchandise |

**Penting:** label “wajib” tidak ditentukan AI secara bebas. Status wajib berasal dari template, kontrak, kebijakan perusahaan, aturan yang relevan, atau keputusan pengguna yang tercatat.

### 3.4 Berdasarkan sifat barang atau jasa

| Kode | Tipe | Penjelasan | Contoh |
|---|---|---|---|
| NAT-CONS | Habis pakai | Digunakan dan umumnya habis dalam satu/ beberapa proyek | Tisu, air mineral, plester |
| NAT-REUS | Dapat digunakan kembali | Menjadi persediaan/aset operasional | Kotak P3K, megafon, payung, kabel ekstensi |
| NAT-RENT | Sewa | Dibayar untuk penggunaan sementara | HT, sound system, perlengkapan event |
| NAT-SVC | Jasa | Pembayaran layanan/tenaga | Guide, fotografer, interpreter |
| NAT-FEE | Fee/administrasi | Biaya layanan atau administrasi | Biaya transfer, booking fee |
| NAT-TAX | Pajak/pungutan | Dicatat sesuai perlakuan transaksi dan aturan | PPN atau pemotongan pajak yang relevan |
| NAT-RES | Cadangan/provisi | Anggaran untuk risiko yang teridentifikasi | Cadangan perubahan harga atau keadaan darurat |

### 3.5 Berdasarkan cara menghitung kuantitas

| Kode | Basis hitung | Satuan contoh |
|---|---|---|
| Q-PAX | Per peserta | pax, orang |
| Q-PAXDAY | Per peserta per hari | pax-hari |
| Q-DAY | Per hari | hari |
| Q-NIGHT | Per malam | malam |
| Q-UNIT | Per unit | unit, kendaraan, kamar |
| Q-TRIP | Per perjalanan/rit | trip, rit |
| Q-KM | Berdasarkan jarak | km |
| Q-HOUR | Berdasarkan waktu | jam |
| Q-ROOM | Per kamar | room-night |
| Q-MEAL | Per porsi/kali makan | porsi |
| Q-SET | Per paket/set | set, paket |
| Q-LOT | Borongan/lumpsum | lot |
| Q-PCT | Persentase dari basis tertentu | % |
| Q-ACTUAL | Berdasarkan realisasi | sesuai bukti/kuantitas aktual |

Satuan harus jelas. Contoh: `2 bus × 3 hari × Rp4.000.000 per bus-hari`, bukan hanya “bus Rp24 juta”.

---

## 4. Master daftar komponen biaya

Daftar di bawah adalah **seed database awal**. Nama item dapat disesuaikan, digandakan untuk variasi layanan, dan ditambah oleh travel agent. Item tidak otomatis berarti wajib dibeli pada setiap proyek.

### MC01 — Transportasi & Mobilitas

#### A. Transportasi darat
- Sewa bus besar per hari/rit.
- Sewa medium bus.
- Sewa minibus.
- Sewa mobil/MPV.
- Sewa SUV/4WD untuk medan khusus.
- Sewa kendaraan VIP.
- Sewa kendaraan operasional/logistik.
- Shuttle antar-jemput.
- Transfer bandara, stasiun, terminal, pelabuhan.
- Kendaraan feeder/angkutan lokal.
- Kendaraan cadangan/pengganti bila dibutuhkan.
- Driver.
- Kernet.
- Uang makan driver/kernet.
- Uang harian driver.
- Penginapan driver/kernet.
- Overtime driver.
- Biaya kelebihan kilometer.
- Biaya standby/tunggu.
- Biaya jemput di luar area.
- Biaya kendaraan kosong/dead mileage.
- BBM.
- Tol.
- Parkir.
- Retribusi/akses kendaraan.
- Penyeberangan kendaraan/ferry.
- Cuci kendaraan.
- Biaya masuk kawasan/terminal jika berlaku.

#### B. Transportasi udara
- Tiket pesawat domestik.
- Tiket pesawat internasional.
- Airport/terminal charge yang belum termasuk tiket.
- Bagasi tercatat.
- Bagasi tambahan/overweight.
- Pemilihan kursi.
- Perubahan jadwal/nama sesuai ketentuan maskapai.
- Biaya pembatalan/no-show.
- Airport transfer.
- Porter/bantuan bagasi bila digunakan.
- Fast track/meet and assist bila dipesan.
- Biaya layanan pemesanan tiket.

#### C. Transportasi kereta
- Tiket kereta.
- Tiket kelas/upgrade.
- Bagasi atau layanan tambahan jika berlaku.
- Biaya perubahan/pembatalan.
- Transfer stasiun.
- Porter/bantuan bagasi.

#### D. Transportasi laut dan lokal
- Tiket kapal penumpang.
- Tiket ferry.
- Tiket speedboat/boat.
- Sewa kapal/perahu.
- Sewa kendaraan lokal.
- Biaya sandar/akses yang berlaku.
- Bagasi/kargo.
- Transfer pelabuhan.
- Biaya keselamatan/perlengkapan khusus jika belum termasuk.

### MC02 — Akomodasi

#### A. Kamar peserta
- Hotel per kamar per malam.
- Villa/rumah sewa.
- Homestay/guest house.
- Resort.
- Dormitory/asrama.
- Tenda/camping ground.
- Paket kamar termasuk sarapan.
- Single supplement.
- Extra bed.
- Connecting room/adjacent room bila diminta.
- Upgrade kamar.
- Perbedaan tarif weekday/weekend.
- High season/peak season surcharge.
- Early check-in.
- Late check-out.
- Tambahan malam.
- Deposit kamar yang dapat dikembalikan (catat sebagai deposit, bukan otomatis biaya).

#### B. Kamar kru dan pendamping
- Kamar tour leader.
- Kamar tour guide/local guide.
- Kamar driver/kernet.
- Kamar staf/event crew.
- Kamar interpreter/pendamping.
- Kamar tenaga medis/keamanan bila menginap.

#### C. Biaya terkait akomodasi
- Biaya pembatalan/no-show.
- Biaya perubahan jumlah kamar.
- Biaya laundry kru bila disepakati.
- Biaya porter.
- Biaya layanan yang belum termasuk.
- Biaya akses/fasilitas yang belum termasuk.

### MC03 — Konsumsi & Hospitality

#### A. Makanan utama
- Sarapan.
- Makan siang.
- Makan malam.
- Lunch box.
- Dinner box.
- Paket prasmanan.
- Paket restoran.
- Konsumsi di perjalanan.
- Konsumsi kru/driver/guide.
- Konsumsi panitia/event crew.

#### B. Snack dan minuman
- Snack box.
- Coffee break.
- Air mineral botol/galon.
- Air minum isi ulang.
- Welcome drink.
- Jus/minuman.
- Kopi/teh.
- Snack cadangan.
- Konsumsi perjalanan malam.

#### C. Kebutuhan khusus
- Vegetarian/vegan meal.
- Halal meal arrangement.
- Makanan khusus alergi.
- Diet atau kebutuhan medis sesuai informasi peserta.
- Kids meal.
- Makanan khusus VIP.
- Makanan kru terpisah bila diperlukan.

#### D. Biaya tambahan konsumsi
- Biaya layanan/service charge.
- Pajak yang dibebankan penyedia jika berlaku.
- Biaya ruang makan privat.
- Biaya corkage atau fasilitas khusus bila relevan.
- Biaya tambahan akibat perubahan jumlah porsi.
- Biaya pembatalan reservasi.

### MC04 — Tiket Wisata & Aktivitas

#### A. Tiket dan akses
- Tiket masuk objek wisata.
- Tiket wisatawan domestik.
- Tiket wisatawan mancanegara.
- Tiket rombongan.
- Tiket anak/dewasa/lansia sesuai tarif.
- Tiket wahana.
- Tiket museum/galeri.
- Tiket pertunjukan.
- Tiket kawasan konservasi/taman nasional jika berlaku.
- Biaya reservasi/booking.
- Biaya akses khusus.
- Biaya parkir objek wisata (jika tidak masuk transportasi).

#### B. Aktivitas dan pengalaman
- Sewa perahu.
- Snorkeling/diving.
- Sewa alat aktivitas.
- Instruktur aktivitas.
- Pemandu aktivitas.
- Fasilitator outbound.
- Paket permainan/team building.
- Workshop/kegiatan budaya.
- Kelas memasak/kerajinan.
- Aktivitas petik hasil kebun/pertanian.
- Camping activity.
- Api unggun dan perlengkapannya.
- Aktivitas olahraga/adventure.
- Sewa perlengkapan keselamatan.
- Biaya dokumentasi aktivitas bila terpisah.

#### C. Kebutuhan khusus aktivitas
- Izin aktivitas.
- Asuransi aktivitas bila tersedia/dipersyaratkan.
- Pendamping khusus.
- Peralatan aksesibilitas.
- Biaya pembatalan karena cuaca/operasional.

### MC05 — SDM, Guide & Tenaga Pelaksana

#### A. Pemandu dan pengelola perjalanan
- Tour leader.
- Tour guide.
- Local guide.
- City guide.
- Interpreter/translator.
- Airport representative.
- Tour coordinator.
- Liaison officer.
- On-site coordinator.
- Koordinator rombongan.

#### B. Kru acara dan layanan
- Event manager.
- Event crew.
- Registrasi.
- Usher.
- MC/presenter.
- Moderator.
- Narasumber/pembicara.
- Fasilitator.
- Instruktur.
- Fotografer.
- Videografer.
- Editor.
- Tim dekorasi.
- Tim teknis.
- Tim keamanan.
- Tim medis.
- Petugas kebersihan.

#### C. Komponen pembayaran SDM
- Honor per hari.
- Honor per kegiatan.
- Honor per jam/overtime.
- Uang harian.
- Uang makan.
- Transport lokal.
- Penginapan.
- Tiket perjalanan.
- Komunikasi/pulsa.
- Tips/uang apresiasi jika disepakati.
- Penggantian biaya (reimbursement).
- Biaya pengganti tenaga/cadangan.

**Catatan:** bedakan honor/jasa profesional, upah tenaga kerja, uang harian, reimbursement, dan tips. Perlakuan pajaknya dapat berbeda.

### MC06 — Perlengkapan, P3K & Kebutuhan Peserta

#### A. P3K dan kesehatan
- Kotak P3K.
- Antimo/obat mabuk perjalanan sesuai kebutuhan dan aturan penggunaan.
- Betadine/antiseptik.
- Plester luka.
- Kasa steril.
- Perban.
- Kapas.
- Cairan pembersih luka.
- Sarung tangan sekali pakai.
- Masker.
- Termometer.
- Koyo.
- Kompres dingin instan.
- Hand sanitizer.
- Kantong muntah.
- Kantong plastik cadangan untuk kebutuhan darurat.
- Obat/perlengkapan khusus sesuai kebijakan dan arahan tenaga kesehatan.
- Biaya pengisian ulang kotak P3K.
- Pemeriksaan masa kedaluwarsa/pergantian stok.

**Peringatan keselamatan:** item obat tidak berarti tour leader bebas mendiagnosis atau memberikan obat. Cantumkan aturan penggunaan, penyimpanan, alergi, tanggal kedaluwarsa, dan prosedur rujukan. Untuk kondisi medis, ikuti arahan tenaga kesehatan dan persetujuan peserta.

#### B. Kebersihan dan sanitasi
- Tisu kering.
- Tisu basah.
- Sabun cuci tangan.
- Hand sanitizer.
- Kantong sampah.
- Plastik kresek berbagai ukuran.
- Lap/kain pembersih.
- Disinfektan sesuai kebutuhan.
- Perlengkapan kebersihan kendaraan/peralatan.
- Sarung tangan kebersihan.
- Pembalut darurat bila relevan dan disediakan.
- Toilet kit/perlengkapan sanitasi bila diperlukan.

#### C. Kebutuhan kenyamanan dan cuaca
- Air mineral cadangan.
- Payung.
- Jas hujan/ponco.
- Selimut perjalanan.
- Bantal leher.
- Kipas portable.
- Sunblock bila termasuk fasilitas.
- Topi.
- Perlengkapan anak.
- Perlengkapan ibadah sesuai kebutuhan.
- Kursi roda/alat bantu mobilitas (sewa atau pembelian).
- Perlengkapan khusus lansia/aksesibilitas.

#### D. Administrasi peserta dan merchandise
- Name tag.
- ID card.
- Lanyard.
- Stiker rombongan.
- Gelang identitas.
- Goodie bag.
- Merchandise.
- Kaos/topi peserta.
- Sertifikat.
- Buku panduan/itinerary cetak.
- Peta/rundown cetak.
- Pulpen dan notes peserta.

#### E. Peralatan operasional reusable
- Megafon.
- HT/radio komunikasi.
- Power bank.
- Charger.
- Kabel ekstensi.
- Adaptor/terminal listrik.
- Senter.
- Lampu portable.
- Gunting.
- Cutter.
- Lakban.
- Tali pengikat.
- Spidol.
- Papan nama/standing sign reusable.
- Jas hujan kru.
- Payung operasional.
- Tas/perlengkapan P3K.
- Timbangan bagasi.
- Peralatan pendukung lainnya.

### MC07 — Produksi Acara, Dokumentasi & Peralatan Teknis

#### A. Venue dan produksi
- Sewa venue/ruang meeting.
- Ballroom.
- Ruang breakout.
- Area outdoor.
- Panggung.
- Backdrop.
- Dekorasi.
- Booth.
- Meja registrasi.
- Kursi/meja tambahan.
- Tenda.
- Penerangan.
- Genset.
- Distribusi listrik.
- Kabel dan instalasi.
- Loading/unloading.
- Setup/dismantle.
- Kebersihan venue.
- Keamanan venue.

#### B. Audio visual dan teknologi
- Sound system.
- Microphone.
- Mixer.
- Speaker tambahan.
- LED screen.
- Proyektor.
- Screen.
- Laptop/komputer.
- Clicker/presenter.
- Lighting.
- Kamera live streaming.
- Internet khusus/bandwidth.
- Teknisi audio visual.
- Operator.
- Perekaman acara.
- Sistem hybrid meeting.
- Perangkat konferensi.

#### C. Dokumentasi dan materi
- Fotografer.
- Videografer.
- Video highlight.
- Video aftermovie.
- Editing.
- Live streaming.
- Desain grafis.
- Percetakan backdrop/banner.
- Dokumentasi drone (dengan izin yang diperlukan).
- Penyimpanan dan distribusi file.
- Album/cetak foto.

#### D. Program dan pengisi acara
- MC.
- Moderator.
- Narasumber.
- Performer/hiburan.
- Musik.
- Aktivitas ice breaking.
- Hadiah/games.
- Penghargaan/trofi.
- Materi acara.
- Lisensi/hak penggunaan materi atau musik bila berlaku.

### MC08 — Administrasi, Komunikasi & Perizinan

#### A. Administrasi dan dokumen
- ATK kantor/proyek.
- Kertas.
- Tinta/toner.
- Fotokopi.
- Cetak itinerary.
- Cetak daftar peserta.
- Cetak manifest.
- Cetak voucher.
- Cetak name list.
- Map/folder.
- Materai sesuai kebutuhan.
- Pengiriman dokumen.
- Kurir.
- Pengarsipan.
- Penerjemahan dokumen.
- Legalisasi/notaris bila diperlukan.

#### B. Komunikasi dan koordinasi
- Pulsa telepon.
- Paket data.
- Internet proyek.
- HT/radio sewa (jika bukan perlengkapan MC06).
- Biaya telekonferensi.
- Komunikasi internasional.
- Biaya koordinasi vendor.
- Biaya rapat proyek.
- Konsumsi rapat.
- Transportasi rapat/survey (jika tidak dicatat di MC01).
- Biaya komunikasi darurat.

#### C. Survey dan persiapan
- Survey lokasi.
- Transport survey.
- Akomodasi survey.
- Konsumsi survey.
- Honor surveyor.
- Uji coba/running test.
- Technical meeting.
- Site inspection.
- Biaya persiapan operasional.

#### D. Perizinan dan kepatuhan
- Izin kegiatan.
- Izin penggunaan lokasi.
- Izin keramaian jika diwajibkan.
- Izin dokumentasi/drone jika diperlukan.
- Izin aktivitas khusus.
- Administrasi kawasan/otoritas.
- Dokumen perjalanan yang menjadi tanggung jawab penyelenggara.
- Konsultasi profesional terkait izin.
- Biaya sertifikasi/pemeriksaan yang relevan.

**Aturan anti-duplikasi:** biaya survey transportasi masuk MC01 jika dicatat sebagai perjalanan; MC08 menampung biaya administrasi/koordinasi surveynya. Satu transaksi hanya boleh memiliki satu kategori utama.

### MC09 — Keuangan, Komisi & Pajak

#### A. Perbankan dan pembayaran
- Biaya transfer antarbank.
- Biaya transfer internasional.
- Biaya administrasi rekening yang dapat dialokasikan.
- Biaya payment gateway.
- MDR/biaya QRIS sesuai ketentuan penyedia.
- Biaya kartu/kartu kredit.
- Biaya pencairan.
- Biaya konversi mata uang.
- Selisih kurs terealisasi.
- Biaya remitansi.
- Biaya pembayaran platform/OTA.
- Biaya refund/transaksi balik.

#### B. Pendanaan dan pembayaran bertempo
- Bunga pinjaman yang relevan.
- Biaya fasilitas kredit.
- Biaya pendanaan modal kerja.
- Biaya keterlambatan pembayaran yang menjadi beban perusahaan.
- Biaya penjaminan/garansi bank bila ada.
- Biaya jaminan penawaran/pelaksanaan sesuai kontrak.
- Biaya administrasi fasilitas pembiayaan.

#### C. Komisi dan kemitraan
- Komisi agen.
- Komisi subagen.
- Referral fee.
- Sales commission.
- Komisi perantara.
- Marketing fee.
- Management fee mitra.
- Bagi hasil mitra sesuai perjanjian.
- Insentif penjualan.
- Komisi kanal distribusi/OTA.

#### D. Pajak dan pungutan
- PPN jika terutang.
- PPh yang dipotong/dipungut pihak lain.
- PPh yang menjadi kewajiban perusahaan.
- Pajak atas jasa/vendor sesuai ketentuan.
- Pajak daerah atau pungutan daerah yang relevan.
- Bea masuk/biaya kepabeanan jika relevan.
- Biaya administrasi perpajakan.
- Denda/bunga pajak jika terjadi dan harus dicatat.

**Peringatan:** jangan menjumlahkan semua pajak sebagai biaya proyek secara otomatis. Sistem harus membedakan pajak keluaran, pajak masukan, pajak dipotong, pajak dibayar, pajak yang dapat dikreditkan, dan pajak yang benar-benar menjadi beban. Aturan bergantung pada status badan usaha, PKP/non-PKP, jenis transaksi, pihak lawan transaksi, lokasi, serta ketentuan yang berlaku. Perlu konfigurasi dan validasi tenaga pajak.

### MC10 — Overhead, Risiko & Cadangan Proyek

#### A. Alokasi overhead perusahaan
- Alokasi gaji staf administrasi.
- Alokasi biaya kantor/sewa.
- Listrik dan air kantor.
- Internet kantor.
- Telepon kantor.
- Software berlangganan.
- Sistem reservasi/operasional.
- Biaya domain/hosting yang dialokasikan.
- Penyusutan laptop/komputer.
- Penyusutan printer/peralatan.
- Penyusutan kendaraan/aset.
- Biaya manajemen.
- Biaya pemasaran umum.
- Biaya akuntansi/pembukuan umum.
- Biaya legal/kepatuhan umum.

**Aturan:** overhead dapat dialokasikan dengan dasar yang konsisten, misalnya persentase pendapatan, jam kerja, jumlah proyek, atau metode lain yang ditetapkan. Jangan memasukkan overhead dua kali jika sudah ada di harga paket/vendor.

#### B. Risiko dan cadangan
- Cadangan perubahan harga vendor.
- Cadangan perubahan kurs.
- Cadangan perubahan jumlah peserta.
- Cadangan cuaca.
- Cadangan keterlambatan.
- Cadangan kendaraan pengganti.
- Cadangan perubahan jadwal.
- Cadangan pembatalan.
- Cadangan kebutuhan medis/darurat.
- Cadangan kehilangan/kerusakan perlengkapan.
- Cadangan refund/kompensasi sesuai kebijakan.
- Cadangan biaya tak terduga yang memiliki dasar risiko.

**Aturan:** contingency bukan angka asal. Simpan alasan risiko, dasar estimasi, metode hitung, dan siapa yang menyetujui. Realisasi cadangan harus dicatat sebagai pengeluaran aktual; sisa cadangan bukan otomatis biaya yang sudah terjadi.

---

## 5. Struktur tampilan dan interaksi

### 5.1 Halaman utama costing

Tampilan ringkas yang disarankan:

1. Header proyek: nama, jenis perjalanan, tanggal, durasi, peserta, level kompleksitas.
2. Ringkasan: total anggaran, HPP per peserta, jumlah kategori, item belum berharga, item belum diverifikasi.
3. Daftar 10 master kategori dalam bentuk accordion.
4. Tombol `Tambah item biaya`.
5. Tombol `Generate ulang daftar` dengan pilihan mempertahankan item manual.
6. Panel `Pemeriksaan kelengkapan`.
7. Ringkasan anggaran dan harga jual.

### 5.2 Tampilan setiap accordion

Setiap kategori menampilkan:
- Kode dan nama kategori.
- Jumlah item aktif.
- Subtotal kategori.
- Status: lengkap/perlu harga/perlu verifikasi/perlu keputusan.
- Tombol buka/tutup.
- Tombol tambah item.

Di dalam accordion tampilkan baris item dengan:
- Nama item.
- Kuantitas dan satuan.
- Harga satuan.
- Total.
- Status klasifikasi.
- Sumber harga.
- Tombol edit/nonaktifkan/hapus dari proyek.

Untuk HP, gunakan daftar/kartu per item; jangan memaksa tabel lebar dengan banyak kolom.

### 5.3 Perilaku edit item

Pengguna dapat:
- Mengubah nama item untuk proyek tersebut.
- Mengubah kuantitas.
- Mengubah satuan.
- Mengubah harga satuan.
- Mengubah mata uang.
- Mengubah kategori/subkategori dengan izin.
- Mengubah klasifikasi dengan alasan.
- Mengisi vendor dan sumber harga.
- Menambah catatan.
- Menandai termasuk dalam paket vendor.
- Menonaktifkan item di proyek.
- Menghapus item dari proyek.
- Menyimpan item baru ke master pribadi (opsional).

Perubahan di satu proyek **tidak boleh mengubah master global** tanpa tindakan khusus.

### 5.4 Status item yang disarankan

| Status | Arti |
|---|---|
| Suggested | Disarankan sistem, belum dikonfirmasi |
| Included | Dipakai dalam anggaran |
| Excluded | Tidak dipakai; alasan dapat dicatat |
| Need quantity | Kuantitas belum diisi |
| Need price | Harga belum diisi |
| Need verification | Harga perlu diverifikasi |
| Quoted | Sudah masuk penawaran vendor |
| Committed | Sudah dipesan/terikat kontrak |
| Actual | Pengeluaran aktual sudah dicatat |
| Cancelled | Dibatalkan |

Status `Actual` sebaiknya berasal dari transaksi/realisasi, bukan sekadar centang manual pada daftar rencana.

---

## 6. Aturan otomatis membuat daftar biaya

Sistem tidak menampilkan seluruh master sekaligus. Sistem membentuk daftar proyek berdasarkan data proyek.

### 6.1 Input yang digunakan
- Jenis perjalanan: domestic, inbound, outbound, corporate/MICE, educational, event/gathering, lainnya.
- Level kompleksitas: Simple, Professional, Enterprise.
- Jumlah peserta dan komposisi peserta.
- Tanggal dan durasi.
- Kota asal, tujuan, negara, dan rute.
- Itinerary per hari.
- Moda transportasi.
- Kebutuhan kendaraan dan kapasitas.
- Kebutuhan kamar dan pola pembagian kamar.
- Pola konsumsi.
- Destinasi dan aktivitas.
- Kebutuhan acara/peralatan.
- Bahasa dan kebutuhan khusus peserta.
- Kontrak/SOW atau permintaan klien jika tersedia.

### 6.2 Urutan proses
1. Pengguna mengisi data dasar proyek.
2. Sistem membaca itinerary dan detail permintaan.
3. Template aturan memilih kandidat komponen biaya.
4. AI memeriksa itinerary untuk menemukan kebutuhan yang mungkin belum terwakili.
5. Sistem menggabungkan kandidat dan menghapus duplikasi berdasarkan kode/aturan.
6. Sistem menghitung kuantitas awal jika datanya tersedia.
7. Sistem menandai item yang membutuhkan harga vendor.
8. Pengguna memeriksa, mengedit, menambah, atau mengecualikan item.
9. Sistem menjalankan pemeriksaan kelengkapan.
10. Setelah disetujui, daftar menjadi baseline anggaran proyek.

### 6.3 Contoh aturan pemunculan

| Kondisi/input | Komponen yang dimunculkan |
|---|---|
| Ada perjalanan bus | Sewa bus, driver, BBM/tol/parkir jika belum termasuk, overtime, biaya kru |
| Perjalanan lebih dari satu hari | Akomodasi kru dan peserta sesuai kebutuhan |
| Ada aktivitas makan | Makan sesuai itinerary, konsumsi kru, air minum |
| Ada perjalanan berliku/jauh atau indikasi rawan mabuk | Kantong muntah dan perlengkapan kenyamanan direkomendasikan |
| Ada peserta anak/lansia | Kebutuhan pendamping/perlengkapan khusus ditanyakan |
| Ada aktivitas outdoor | Perlengkapan cuaca, P3K, keselamatan, instruktur bila perlu |
| Ada penerbangan | Tiket, bagasi, transfer, perubahan/pembatalan sesuai kebijakan |
| Inbound | Meet & greet, interpreter/guide bahasa, SIM/eSIM atau komunikasi lokal bila perlu |
| Outbound | Paspor/visa checklist, asuransi, bagasi, kurs, biaya transaksi luar negeri sesuai kebutuhan |
| MICE/event | Venue, AV, registrasi, backdrop, kru, dokumentasi, setup/dismantle |
| Ada survey | Transport, akomodasi, konsumsi, honor surveyor, biaya koordinasi sesuai kebutuhan |
| Ada vendor paket lumpsum | Sistem meminta rincian inclusion/exclusion agar tidak double costing |

Aturan harus dapat dikonfigurasi dan memiliki versi. Jangan membuat asumsi otomatis yang tidak bisa dijelaskan.

### 6.4 Profil tampilan berdasarkan level

**Simple**
- Tampilkan item inti dan rekomendasi yang relevan.
- Kategori yang belum relevan tetap dapat dibuka melalui `Lihat kategori lainnya`.
- Detail teknis dan audit lanjutan disembunyikan secara default.
- Tetap ada peringatan item wajib yang belum diisi.

**Professional**
- Tampilkan seluruh kategori yang relevan.
- Aktifkan perbandingan vendor, alokasi kru, rencana vs aktual, dan cash flow proyek.
- Item kondisional dan risiko tampil sebagai checklist.

**Enterprise**
- Tampilkan seluruh kategori dan rincian.
- Aktifkan approval, multi-vendor, multi-currency, termin, retensi, jaminan, audit trail, serta struktur RAB sesuai kebutuhan kontrak.
- Mendukung multi-grup, multi-kota, multi-hari, dan pembagian cost center.

**Catatan:** skala proyek dapat dinaikkan untuk satu pekerjaan tanpa mengubah profil permanen perusahaan.

---

## 7. Struktur data yang disarankan

Gunakan master terpisah dari item anggaran proyek. Ini penting agar harga dan perubahan di satu proyek tidak merusak master.

### 7.1 Tabel `cost_categories`

| Field | Tipe | Keterangan |
|---|---|---|
| id | UUID | Primary key |
| code | TEXT | MC01–MC10, unik |
| name | TEXT | Nama kategori |
| description | TEXT | Penjelasan |
| sort_order | INT | Urutan tampilan |
| is_active | BOOLEAN | Aktif/nonaktif |
| created_at | TIMESTAMP | Waktu dibuat |
| updated_at | TIMESTAMP | Waktu diperbarui |

### 7.2 Tabel `cost_subcategories`

| Field | Tipe | Keterangan |
|---|---|---|
| id | UUID | Primary key |
| category_id | UUID | FK ke cost_categories |
| code | TEXT | Kode subkategori |
| name | TEXT | Nama |
| description | TEXT | Penjelasan |
| sort_order | INT | Urutan |
| is_active | BOOLEAN | Status |

### 7.3 Tabel `cost_items` — master komponen biaya

| Field | Tipe | Keterangan |
|---|---|---|
| id | UUID | Primary key |
| code | TEXT | Kode item stabil dan unik |
| subcategory_id | UUID | FK subkategori |
| name | TEXT | Nama komponen |
| description | TEXT | Definisi item |
| default_unit | TEXT | Satuan default |
| default_quantity_basis | TEXT | Q-PAX, Q-DAY, dll. |
| cost_relation | TEXT | COST-DIR/IND/MIX |
| cost_behavior | TEXT | BEH-FIX/VAR/STEP/MIX |
| usage_class | TEXT | USE-REQ/REC/CND/OPT |
| nature_type | TEXT | NAT-CONS/REUS/RENT/SVC/FEE/TAX/RES |
| default_currency | CHAR(3) | Mata uang default, mis. IDR |
| default_price | NUMERIC | Harga referensi opsional |
| price_source | TEXT | Sumber harga referensi |
| price_valid_until | DATE | Masa berlaku harga |
| verification_status | TEXT | unverified/verified/expired |
| applicable_trip_types | JSONB | Jenis perjalanan yang relevan |
| applicable_levels | JSONB | Level tampilan yang relevan |
| trigger_rules | JSONB | Kondisi pemunculan |
| default_inclusions | JSONB | Komponen yang biasanya sudah termasuk |
| safety_note | TEXT | Catatan keselamatan |
| tax_profile_id | UUID | Referensi profil pajak, bila digunakan |
| is_global | BOOLEAN | Master global atau khusus organisasi |
| owner_org_id | UUID | Pemilik master khusus organisasi |
| is_active | BOOLEAN | Aktif/nonaktif |
| version | INT | Versi item master |
| created_at | TIMESTAMP | Waktu dibuat |
| updated_at | TIMESTAMP | Waktu diperbarui |

**Catatan:** `default_price` bukan harga final yang otomatis dipakai. Harga proyek harus menyimpan snapshot harga, sumber, tanggal, dan vendor yang dipakai saat costing dibuat.

### 7.4 Tabel `projects`

| Field | Tipe | Keterangan |
|---|---|---|
| id | UUID | Primary key |
| project_code | TEXT | Kode proyek |
| project_name | TEXT | Nama proyek |
| trip_type | TEXT | Domestic/inbound/outbound/MICE/dll. |
| complexity_level | TEXT | simple/professional/enterprise |
| start_date | DATE | Tanggal mulai |
| end_date | DATE | Tanggal selesai |
| pax_count | INT | Jumlah peserta |
| origin | TEXT | Titik asal |
| destinations | JSONB | Daftar tujuan/rute |
| itinerary | JSONB | Rencana kegiatan per hari |
| currency | CHAR(3) | Mata uang dasar proyek |
| status | TEXT | draft/quoted/approved/ongoing/closed |
| created_at | TIMESTAMP | Waktu dibuat |
| updated_at | TIMESTAMP | Waktu diperbarui |

### 7.5 Tabel `project_cost_items` — item anggaran per proyek

| Field | Tipe | Keterangan |
|---|---|---|
| id | UUID | Primary key |
| project_id | UUID | FK ke projects |
| master_cost_item_id | UUID | FK ke cost_items; boleh null untuk item custom |
| item_code_snapshot | TEXT | Kode pada saat item dimasukkan |
| item_name | TEXT | Nama snapshot/proyek |
| category_id | UUID | Kategori |
| subcategory_id | UUID | Subkategori |
| quantity | NUMERIC | Kuantitas |
| unit | TEXT | Satuan |
| unit_price | NUMERIC | Harga satuan |
| currency | CHAR(3) | Mata uang item |
| exchange_rate | NUMERIC | Kurs ke mata uang proyek |
| exchange_rate_date | DATE | Tanggal kurs |
| amount_original | NUMERIC | Total dalam mata uang asal |
| amount_project_currency | NUMERIC | Total dalam mata uang proyek |
| usage_class | TEXT | Wajib/rekomendasi/kondisional/opsional |
| cost_relation | TEXT | Langsung/tidak langsung/campuran |
| cost_behavior | TEXT | Tetap/variabel/bertingkat/campuran |
| nature_type | TEXT | Habis pakai/reusable/sewa/jasa/dll. |
| item_status | TEXT | Suggested/Included/Excluded/Need price/dll. |
| vendor_id | UUID | Vendor jika ada |
| price_source | TEXT | Penawaran/histori/estimasi |
| price_checked_at | TIMESTAMP | Tanggal verifikasi |
| included_in_vendor_package | BOOLEAN | Apakah sudah termasuk paket vendor |
| inclusion_note | TEXT | Rincian inclusion/exclusion |
| is_manual_item | BOOLEAN | Item ditambahkan manual |
| exclusion_reason | TEXT | Alasan dikeluarkan |
| notes | TEXT | Catatan |
| created_by | UUID | Pembuat |
| updated_by | UUID | Pengubah |
| created_at | TIMESTAMP | Waktu dibuat |
| updated_at | TIMESTAMP | Waktu diubah |

### 7.6 Tabel pendukung yang disarankan

| Tabel | Fungsi |
|---|---|
| `vendors` | Database penyedia barang/jasa |
| `vendor_price_history` | Histori harga per vendor, item, tanggal, dan masa berlaku |
| `cost_item_rules` | Aturan pemunculan item otomatis |
| `cost_templates` | Template costing per jenis perjalanan/level |
| `cost_template_items` | Daftar item dalam template |
| `project_cost_revisions` | Histori perubahan anggaran/item |
| `project_expenses` | Pengeluaran aktual |
| `expense_receipts` | Bukti nota/foto/file |
| `project_approvals` | Persetujuan anggaran/perubahan |
| `inventory_items` | Barang reusable dan stok |
| `inventory_movements` | Barang keluar, kembali, rusak, atau habis |
| `tax_profiles` | Konfigurasi perlakuan pajak yang dapat diperbarui |
| `exchange_rates` | Kurs dan sumber kurs |
| `cost_allocations` | Alokasi overhead dan biaya bersama |

Tabel pendukung dapat dibangun bertahap. Untuk tahap awal, prioritaskan tabel kategori, subkategori, master item, proyek, item biaya proyek, dan aturan template.

---

## 8. Aturan hitung dasar

### 8.1 Total item
`total_item = kuantitas × harga_satuan`

Jika ada faktor hari, peserta, kamar, atau jam, faktor tersebut harus masuk ke kuantitas terstruktur atau rumus yang tervalidasi.

Contoh:
`2 bus × 3 hari × Rp4.000.000 per bus-hari = Rp24.000.000`

### 8.2 Biaya per peserta
`biaya_per_peserta = total_biaya_yang_dialokasikan / jumlah_peserta`

Jangan membagi semua biaya secara buta jika ada komponen yang dibayar per kamar, per kendaraan, per grup, atau per proyek. Total biaya proyek tetap menjadi dasar; alokasi per peserta hanya metode penyajian.

### 8.3 Barang reusable
Barang reusable tidak otomatis dibebankan penuh ke satu tour jika masih dipakai untuk proyek lain. Pilih salah satu:
- Pembelian aset/persediaan oleh perusahaan.
- Sewa/penggunaan per proyek.
- Alokasi biaya penggunaan/penyusutan berdasarkan kebijakan.

### 8.4 Deposit dan uang jaminan
Deposit yang dapat dikembalikan harus dicatat sebagai uang muka/deposit, bukan langsung sebagai biaya. Jika kemudian dipotong vendor, bagian yang dipotong dicatat sesuai sifat transaksinya.

### 8.5 Anggaran, komitmen, aktual
- **Budget:** rencana biaya.
- **Committed:** pesanan/kontrak yang sudah disetujui.
- **Actual:** biaya yang benar-benar terjadi/diakui sesuai kebijakan pembukuan.
- **Paid:** uang yang sudah dibayarkan.

Keempatnya jangan disamakan. Tagihan belum tentu sudah dibayar; pembayaran deposit belum tentu seluruhnya menjadi biaya.

---

## 9. Checklist kualitas sebelum costing dinyatakan siap

- [ ] Jenis perjalanan dan level proyek benar.
- [ ] Itinerary dan durasi sudah diperiksa.
- [ ] Jumlah peserta dan komposisi kamar benar.
- [ ] Semua transportasi dan transfer sudah dihitung.
- [ ] Inclusion/exclusion vendor sudah diperiksa agar tidak double costing.
- [ ] Akomodasi peserta dan kru sudah dihitung.
- [ ] Konsumsi peserta dan kru sudah dihitung.
- [ ] Tiket dan aktivitas sesuai itinerary.
- [ ] Honor, uang harian, overtime, dan akomodasi kru sudah diperiksa.
- [ ] P3K, kebersihan, kantong muntah, dan perlengkapan peserta sudah dipertimbangkan.
- [ ] Kebutuhan event/dokumentasi/teknis sudah diperiksa jika relevan.
- [ ] Administrasi, survey, komunikasi, dan perizinan sudah diperiksa.
- [ ] Komisi, biaya transaksi, dan pajak sudah diklasifikasikan.
- [ ] Overhead dan contingency memiliki dasar perhitungan.
- [ ] Harga vendor memiliki sumber dan tanggal verifikasi.
- [ ] Item tanpa harga ditandai, bukan dianggap nol tanpa persetujuan.
- [ ] Item yang dikeluarkan memiliki alasan jika penting.
- [ ] Tidak ada item ganda.
- [ ] Perhitungan kuantitas, subtotal, dan total tervalidasi.
- [ ] Anggaran proyek dan kebutuhan modal kerja sudah diperiksa sebelum quotation.

---

## 10. Rekomendasi implementasi bertahap

### Tahap A — Fondasi master
1. Buat 10 kategori dan subkategori.
2. Masukkan seed item dari dokumen ini.
3. Beri kode item stabil.
4. Isi satuan dan klasifikasi default.
5. Sediakan fitur tambah/edit/nonaktifkan.

### Tahap B — Generator daftar proyek
1. Buat template berdasarkan jenis perjalanan.
2. Tambahkan filter level Simple/Professional/Enterprise.
3. Tambahkan aturan pemunculan berdasarkan itinerary dan kondisi.
4. Tampilkan item sebagai Suggested.
5. Pengguna konfirmasi menjadi Included atau Excluded.

### Tahap C — Costing
1. Isi kuantitas, satuan, harga, vendor, dan sumber.
2. Hitung subtotal otomatis.
3. Tandai harga belum diverifikasi/kedaluwarsa.
4. Cegah duplikasi inclusion vendor.
5. Simpan snapshot harga untuk proyek.

### Tahap D — Pengeluaran aktual
1. Catat pengeluaran dan bukti.
2. Hubungkan ke item anggaran bila sesuai.
3. Bandingkan budget, committed, actual, dan paid.
4. Catat persediaan reusable yang kembali.
5. Evaluasi selisih setelah proyek selesai.

---

## 11. Keputusan yang perlu dipertahankan saat pengembangan

- Jangan membuat master kategori terpisah untuk setiap level travel agent.
- Jangan mengunci daftar item; pengguna harus bisa menambah item custom.
- Jangan menghapus master item saat item tidak dipakai dalam satu proyek.
- Jangan menganggap harga kosong sama dengan nol.
- Jangan menganggap semua item rekomendasi harus dibeli.
- Jangan memasukkan pajak dengan satu persentase universal.
- Jangan membebankan seluruh pembelian reusable ke satu tour tanpa kebijakan.
- Jangan menyamakan deposit, biaya, tagihan, dan pembayaran.
- Jangan membiarkan AI menjadi sumber angka final tanpa sumber harga dan validasi.
- Simpan histori perubahan agar angka dalam quotation yang sudah dikirim tetap dapat ditelusuri.

**Hasil yang dituju:** travel agent kecil melihat daftar yang sederhana dan relevan; travel agent menengah mendapat detail operasional yang cukup; travel agent besar dapat membuka seluruh rincian dan kontrol proyek. Ketiganya menggunakan master data dan mesin hitung yang sama.
