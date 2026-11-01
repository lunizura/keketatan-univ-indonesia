# Indeks & Kalkulator Keketatan Perguruan Tinggi Top Indonesia
### Indonesian Top Universities Selectivity & Choice Portfolio Simulator (Top 50 PTN & PTS)

Repositori ini menyajikan basis data analitis dan platform visualisasi tingkat persaingan (keketatan), daya tampung, serta riwayat peminat program studi pada 50 Perguruan Tinggi Negeri (PTN) dan Perguruan Tinggi Swasta (PTS) terkemuka di Indonesia (35 PTN & 15 PTS) yang mencakup 5 wilayah kepulauan (Jawa, Sumatera, Kalimantan, Sulawesi, dan Bali-Nusa Tenggara) dengan total 295 program studi terdata untuk jalur SNBP, SNBT (UTBK), dan SPMB.

[![CI](https://github.com/lunizura/keketatan-univ-indonesia/actions/workflows/ci.yml/badge.svg)](https://github.com/lunizura/keketatan-univ-indonesia/actions)
[![Dataset](https://img.shields.io/badge/Dataset-295%20Prodi-blue.svg)](data/ptn_keketatan.json)
[![Universities](https://img.shields.io/badge/Universitas-50%20(35%20PTN%20%2B%2015%20PTS)-emerald.svg)](data/metadata.json)
[![Regions](https://img.shields.io/badge/Wilayah-5%20Region%20Nusantara-purple.svg)](data/metadata.json)
[![Contributing](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)
[![Bilingual](https://img.shields.io/badge/Languages-ID%20%7C%20EN-gray.svg)](https://lunizura.github.io/keketatan-univ-indonesia/)

---

## Bahasa Indonesia

### 1. Latar Belakang & Tujuan
Setiap tahun, ratusan ribu calon mahasiswa baru menghadapi dilema dalam menentukan pilihan program studi pada seleksi nasional penerimaan mahasiswa baru (SNBP dan SNBT) serta seleksi perguruan tinggi swasta terkemuka. Ketimpangan informasi mengenai rasio persaingan nyata (*selectivity ratio*) kerap mengakibatkan pemilihan kombinasi jurusan yang terlalu berisiko (*high-risk portfolio*), ketiadaan jaring pengaman (*safety net*), atau urutan pilihan yang tidak realistis.

Platform ini hadir untuk menyediakan transparansi berbasis data resmi (*open educational data*) agar calon mahasiswa dapat:
- Mengetahui perbandingan riil antara kuota kursi yang tersedia dengan jumlah peminat tahun-tahun sebelumnya pada 50 kampus terbaik di Indonesia.
- Mengidentifikasi jurusan-jurusan dengan tingkat persaingan paling ketat secara nasional maupun regional.
- Membandingkan program studi sejenis lintas kampus PTN dan PTS (misal: Teknik Informatika di ITB vs UI vs UGM vs ITS vs Telkom University vs Binus University).
- Mensimulasikan dan menguji kelayakan kombinasi Pilihan 1 dan Pilihan 2 secara objektif, termasuk strategi kombinasi hibrida (PTN + PTS) sebagai jaring pengaman berdaya saing tinggi.

---

### 2. Metodologi & Formula Perhitungan

Data diolah menggunakan dua metrik kuantitatif baku:

#### A. Persentase Keketatan (Selectivity Rate)
$$\text{Keketatan} = \left( \frac{\text{Daya Tampung}}{\text{Jumlah Peminat Terakhir}} \right) \times 100\%$$
*Semakin rendah persentasenya, semakin ketat persaingan dan semakin kecil probabilitas lolos.*

Klasifikasi Tingkat Keketatan:
- **Sangat Ketat:** $< 2.50\%$ (Persaingan puncak nasional, rasio di atas $1 : 40$).
- **Ketat:** $2.50\% - 5.00\%$ (Persaingan tinggi, rasio sekitar $1 : 20$ hingga $1 : 40$).
- **Sedang:** $5.01\% - 10.00\%$ (Persaingan moderat, rasio sekitar $1 : 10$ hingga $1 : 20$).
- **Terbuka:** $> 10.00\%$ (Peluang relatif lebih terbuka, rasio di bawah $1 : 10$).

#### B. Rasio Persaingan (Competition Ratio)
$$\text{Rasio} = 1 : \left\lceil \frac{\text{Jumlah Peminat}}{\text{Daya Tampung}} \right\rceil$$
*Contoh:* Rasio $1 : 55$ menandakan bahwa setiap 1 kursi daya tampung diperebutkan oleh 55 orang pendaftar.

---

### 3. Struktur Dokumentasi & Direktori Referensi (Docs Inventory)

Platform ini dilengkapi dengan basis dokumentasi komprehensif yang mencakup glosarium metrik, panduan analitis strategis, profil selektivitas universitas unggulan, serta skrip analitika distribusi:

#### A. Glosarium & Standar Metrik Teknis (`docs/glossary/`)
- [Formula & Metrik Keketatan](docs/glossary/keketatan_metrics.md): Definisi matematika rasio persaingan, rumus normalisasi persentase, dan klasifikasi ambang batas kompetisi.
- [Mekanisme & Kuota Jalur SNBP](docs/glossary/snbp_mechanisms.md): Tata kelola kuota akreditasi sekolah (40%/25%/5%), sistem pemeringkatan elibilitas siswa, dan faktor sertifikat prestasi.
- [Standar Skor UTBK & Desil SNBT](docs/glossary/snbt_utbk_scoring.md): Struktur subtes Tes Potensi Skolastik (TPS), Literasi Bahasa, Penalaran Matematika, dan rentang desil skor.
- [Daya Tampung & Pergeseran Kapasitas](docs/glossary/daya_tampung.md): Analisis pergeseran alokasi kursi minimum SNBP (20%), SNBT (40%), dan Mandiri (maksimal 30-50%).
- [Konversi Akreditasi BAN-PT & LAM](docs/glossary/akreditasi.md): Panduan kesetaraan status Akreditasi Unggul, Baik Sekali, Baik terhadap standar mutu nasional.

#### B. Panduan Analitis Strategis (`docs/guides/`)
- [Optimasi Portofolio Risiko SNBP & SNBT](docs/guides/portfolio_strategy.md): Panduan mitigasi risiko pemilihan 2 program studi, aturan urutan prioritas non-inversi, dan formasi jaring pengaman.
- [Analisis Disparitas Selektivitas Regional](docs/guides/regional_analysis.md): Kajian analitis komparatif tingkat keketatan antara klaster Pulau Jawa vs luar Pulau Jawa.

#### C. Profil Selektivitas 26 Institusi Unggulan (`docs/universities/`)
Profil institusional mendalam menyajikan ringkasan kelembagaan, tabel keketatan program studi terfavorit, serta informasi seleksi mandiri resmi:
- **Jawa:**
  - [Universitas Indonesia (UI)](docs/universities/ui.md)
  - [Institut Teknologi Bandung (ITB)](docs/universities/itb.md)
  - [Universitas Gadjah Mada (UGM)](docs/universities/ugm.md)
  - [Universitas Airlangga (UNAIR)](docs/universities/unair.md)
  - [Institut Teknologi Sepuluh Nopember (ITS)](docs/universities/its.md)
  - [Universitas Padjadjaran (UNPAD)](docs/universities/unpad.md)
  - [Universitas Diponegoro (UNDIP)](docs/universities/undip.md)
  - [Institut Pertanian Bogor (IPB)](docs/universities/ipb.md)
  - [Universitas Brawijaya (UB)](docs/universities/ub.md)
  - [Universitas Sebelas Maret (UNS)](docs/universities/uns.md)
  - [Universitas Negeri Yogyakarta (UNY)](docs/universities/uny.md)
  - [Universitas Negeri Semarang (UNNES)](docs/universities/unnes.md)
  - [Universitas Pendidikan Indonesia (UPI)](docs/universities/upi.md)
  - [Universitas Negeri Jakarta (UNJ)](docs/universities/unj.md)
  - [Universitas Jenderal Soedirman (UNSOED)](docs/universities/unsoed.md)
  - [Telkom University (TELKOM)](docs/universities/telkom.md)
  - [Bina Nusantara University (BINUS)](docs/universities/binus.md)
- **Sumatera:**
  - [Universitas Sumatera Utara (USU)](docs/universities/usu.md)
  - [Universitas Andalas (UNAND)](docs/universities/unand.md)
  - [Universitas Sriwijaya (UNSRI)](docs/universities/unsri.md)
  - [Universitas Lampung (UNILA)](docs/universities/unila.md)
  - [Universitas Syiah Kuala (USK)](docs/universities/usk.md)
  - [Universitas Riau (UNRI)](docs/universities/unri.md)
- **Sulawesi:**
  - [Universitas Hasanuddin (UNHAS)](docs/universities/unhas.md)
  - [Universitas Sam Ratulangi (UNSRAT)](docs/universities/unsrat.md)
- **Bali-Nusa Tenggara:**
  - [Universitas Udayana (UNUD)](docs/universities/unud.md)

#### D. Perangkat Analisis Data Desil (`scripts/` & `data/`)
- [Skrip Ekspor Desil Keketatan Nasional](scripts/export_selectivity_deciles.py): Perangkat kalkulasi distribusi desil D1-D9 untuk jalur SNBP dan SNBT secara menyeluruh dan per-rumpun.
- [Dataset Distribusi Desil](data/selectivity_deciles.json): Keluaran statistik siap pakai yang merinci ambang batas kuartil dan desil nasional.

---

### 4. Cakupan 50 Perguruan Tinggi Top Indonesia (35 PTN & 15 PTS)

Basis data mencakup 50 institusi pendidikan tinggi terakreditasi Unggul di 5 wilayah nusantara:

| No | Singkatan | Nama Lengkap Perguruan Tinggi | Tipe | Wilayah | Kota / Lokasi | Akreditasi | Status Klaster |
| :---: | :--- | :--- | :---: | :---: | :--- | :---: | :---: |
| 1 | UI | Universitas Indonesia | PTN | Jawa | Depok | Unggul | PTN-BH |
| 2 | ITB | Institut Teknologi Bandung | PTN | Jawa | Bandung | Unggul | PTN-BH |
| 3 | UGM | Universitas Gadjah Mada | PTN | Jawa | Sleman / Yogyakarta | Unggul | PTN-BH |
| 4 | IPB | IPB University | PTN | Jawa | Bogor | Unggul | PTN-BH |
| 5 | UNAIR | Universitas Airlangga | PTN | Jawa | Surabaya | Unggul | PTN-BH |
| 6 | ITS | Institut Teknologi Sepuluh Nopember | PTN | Jawa | Surabaya | Unggul | PTN-BH |
| 7 | UNDIP | Universitas Diponegoro | PTN | Jawa | Semarang | Unggul | PTN-BH |
| 8 | UB | Universitas Brawijaya | PTN | Jawa | Malang | Unggul | PTN-BH |
| 9 | UNPAD | Universitas Padjadjaran | PTN | Jawa | Sumedang / Bandung | Unggul | PTN-BH |
| 10 | UNS | Universitas Sebelas Maret | PTN | Jawa | Surakarta | Unggul | PTN-BH |
| 11 | UPI | Universitas Pendidikan Indonesia | PTN | Jawa | Bandung | Unggul | PTN-BH |
| 12 | UNSOED | Universitas Jenderal Soedirman | PTN | Jawa | Purwokerto | Unggul | PTN-BLU |
| 13 | UNY | Universitas Negeri Yogyakarta | PTN | Jawa | Yogyakarta | Unggul | PTN-BH |
| 14 | UNNES | Universitas Negeri Semarang | PTN | Jawa | Semarang | Unggul | PTN-BH |
| 15 | UNESA | Universitas Negeri Surabaya | PTN | Jawa | Surabaya | Unggul | PTN-BH |
| 16 | UM | Universitas Negeri Malang | PTN | Jawa | Malang | Unggul | PTN-BH |
| 17 | UNJ | Universitas Negeri Jakarta | PTN | Jawa | Jakarta Timur | Unggul | PTN-BH |
| 18 | UPNVJ | UPN Veteran Jakarta | PTN | Jawa | Jakarta Selatan | Unggul | PTN-BLU |
| 19 | UPNVYK | UPN Veteran Yogyakarta | PTN | Jawa | Sleman | Unggul | PTN-BLU |
| 20 | UPNVJT | UPN Veteran Jawa Timur | PTN | Jawa | Surabaya | Unggul | PTN-BLU |
| 21 | UNTIRTA | Universitas Sultan Ageng Tirtayasa | PTN | Jawa | Serang | Unggul | PTN-BLU |
| 22 | USU | Universitas Sumatera Utara | PTN | Sumatera | Medan | Unggul | PTN-BH |
| 23 | UNAND | Universitas Andalas | PTN | Sumatera | Padang | Unggul | PTN-BH |
| 24 | UNSRI | Universitas Sriwijaya | PTN | Sumatera | Palembang / Indralaya | Unggul | PTN-BH |
| 25 | UNILA | Universitas Lampung | PTN | Sumatera | Bandar Lampung | Unggul | PTN-BLU |
| 26 | UNP | Universitas Negeri Padang | PTN | Sumatera | Padang | Unggul | PTN-BH |
| 27 | USK | Universitas Syiah Kuala | PTN | Sumatera | Banda Aceh | Unggul | PTN-BH |
| 28 | UNRI | Universitas Riau | PTN | Sumatera | Pekanbaru | Unggul | PTN-BLU |
| 29 | UNMUL | Universitas Mulawarman | PTN | Kalimantan | Samarinda | Unggul | PTN-BLU |
| 30 | ULM | Universitas Lambung Mangkurat | PTN | Kalimantan | Banjarmasin | Unggul | PTN-BLU |
| 31 | UNTAN | Universitas Tanjungpura | PTN | Kalimantan | Pontianak | Unggul | PTN-BLU |
| 32 | UNHAS | Universitas Hasanuddin | PTN | Sulawesi | Makassar | Unggul | PTN-BH |
| 33 | UNSRAT | Universitas Sam Ratulangi | PTN | Sulawesi | Manado | Unggul | PTN-BLU |
| 34 | UNUD | Universitas Udayana | PTN | Bali-Nusa Tenggara | Badung / Denpasar | Unggul | PTN-BLU |
| 35 | UNRAM | Universitas Mataram | PTN | Bali-Nusa Tenggara | Mataram | Unggul | PTN-BLU |
| 36 | TELKOM | Telkom University | PTS | Jawa | Bandung | Unggul | PTS Unggul |
| 37 | BINUS | Bina Nusantara University | PTS | Jawa | Jakarta Barat | Unggul | PTS Unggul |
| 38 | UII | Universitas Islam Indonesia | PTS | Jawa | Sleman | Unggul | PTS Unggul |
| 39 | UMY | Universitas Muhammadiyah Yogyakarta | PTS | Jawa | Bantul | Unggul | PTS Unggul |
| 40 | UNPAR | Universitas Katolik Parahyangan | PTS | Jawa | Bandung | Unggul | PTS Unggul |
| 41 | ATMAJAYA | Unika Atma Jaya | PTS | Jawa | Jakarta Selatan | Unggul | PTS Unggul |
| 42 | UPH | Universitas Pelita Harapan | PTS | Jawa | Tangerang | Unggul | PTS Unggul |
| 43 | TRISAKTI | Universitas Trisakti | PTS | Jawa | Jakarta Barat | Unggul | PTS Unggul |
| 44 | UNTAR | Universitas Tarumanagara | PTS | Jawa | Jakarta Barat | Unggul | PTS Unggul |
| 45 | UMN | Universitas Multimedia Nusantara | PTS | Jawa | Tangerang | Unggul | PTS Unggul |
| 46 | PETRA | Universitas Kristen Petra | PTS | Jawa | Surabaya | Unggul | PTS Unggul |
| 47 | UMS | Universitas Muhammadiyah Surakarta | PTS | Jawa | Surakarta | Unggul | PTS Unggul |
| 48 | PRESUNIV | President University | PTS | Jawa | Cikarang | Unggul | PTS Unggul |
| 49 | USD | Universitas Sanata Dharma | PTS | Jawa | Sleman / Yogyakarta | Unggul | PTS Unggul |
| 50 | MERCU | Universitas Mercu Buana | PTS | Jawa | Jakarta Barat | Unggul | PTS Unggul |

---

### 5. Fitur Utama Platform

1. **Peringkat Terketat Nasional (National Leaderboard):**
   - Menampilkan Top 50 jurusan dengan tingkat keketatan paling kompetitif di Indonesia.
   - Filter dinamis berdasarkan:
     - Jalur seleksi (SNBT vs SNBP).
     - Rumpun keilmuan (Saintek vs Soshum).
     - Tipe institusi (Semua, Hanya PTN, Hanya PTS).
     - Wilayah geografis (Semua, Jawa, Sumatera, Kalimantan, Sulawesi, Bali-Nusa Tenggara).
   - Lencana status visual PTN/PTS dan tag wilayah untuk setiap baris data.

2. **Komparasi Antar-Kampus (Head-to-Head Comparison):**
   - Membandingkan kuota daya tampung, peminat, dan rasio persaingan program studi sejenis di 50 universitas.
   - Visualisasi kartu ringkasan komparasi lengkap dengan indikator kampus terketat versus kampus paling rasional/terbuka.

3. **Kalkulator & Simulator Strategi Portofolio (Choice Portfolio Simulator):**
   - Menguji kombinasi Pilihan 1 dan Pilihan 2 calon mahasiswa dari seluruh 50 kampus.
   - Deteksi otomatis profil risiko:
     - *Risiko Ekstrem:* Kedua pilihan berkeketatan $< 2.5\%$.
     - *Urutan Terbalik:* Pilihan 2 justru memiliki persaingan lebih ketat daripada Pilihan 1.
     - *Strategi Hibrida Berimbang:* Pilihan 1 PTN bergengsi dikombinasikan dengan Pilihan 2 PTS Unggul sebagai jaring pengaman berkualitas tinggi.
   - Dilengkapi preset siap pakai (Teknik Hibrida PTN-PTS, Kedokteran Hibrida PTN-PTS, dan kombinasi murni PTN).

4. **Direktori Jelajah & Modal Detail:**
   - Filter komprehensif berdasarkan rumpun, wilayah geografis, tipe institusi, kampus spesifik, dan rentang keketatan.
   - Modal detail program studi dengan grafik tren riwayat peminat 3 tahun terakhir (2022, 2023, 2024), kurikulum inti, prospek karir lulusan, serta tautan portal SPMB resmi institusi.

5. **Dukungan Dwibahasa Penuh:**
   - Beralih antara Bahasa Indonesia dan English secara instan dengan sinkronisasi parameter URL (`?lang=en` atau `?lang=id`).

---

### 6. Struktur Berkas & Data Terbuka (Open Data)

Dataset disediakan secara terbuka dan terstandardisasi dalam beberapa format:
- `data/ptn_keketatan.json`: Dataset format JSON lengkap mencakup 295 prodi pada 50 universitas.
- `data/ptn_keketatan.js`: Format JavaScript runtime siap pakai untuk antarmuka web statis.
- `data/ptn_keketatan.csv`: Format tabular CSV untuk analisis statistik, Google Sheets, dan pandas.
- `data/selectivity_deciles.json`: Distribusi desil dan metrik kuartil nasional untuk SNBP dan SNBT.
- `data/metadata.json`: Metadata pembaruan, total entri institusi dan program studi, serta lisensi.
- `scripts/build_ptn_dataset.py`: Skrip otomasi Python untuk kompilasi dan regenerasi dataset.
- `scripts/export_selectivity_deciles.py`: Skrip kalkulasi distribusi desil dan ringkasan eksekutif.

---

### 7. Desain Antarmuka & Arsitektur Visual (Editorial Data-Journalism)

Antarmuka web (`index.html`) mengadopsi standar visual jurnalisme data institusional:
- **Sistem Palet Obsidian & Indigo:** Memadukan warna obsidian gelap (`#0a1128`, `#001f54`) pada area masthead dan hero dengan latar kanvas pualam hangat (`#f8fafc`) serta garis batas halus (`#e2e8f0`).
- **Tipografi Dual-Engine:** Menggunakan `Plus Jakarta Sans` untuk judul dan teks naratif, serta `JetBrains Mono` (`font-variant-numeric: tabular-nums`) untuk penyelarasan data kuota, pendaftar, dan rasio.
- **Medali Peringkat & Indikator Kepadatan Persaingan:** Peringkat Top 3 dilengkapi medali emas, perak, dan perunggu. Rasio persaingan (1 : N) dilengkapi meteran batang horizontal interaktif yang merefleksikan tingkat risiko kursi secara visual.
- **Kartu Evaluasi Strategi Cerdas:** Hasil simulasi portofolio disajikan dengan garis batas aksen warna, indikator status risiko, dan rekomendasi mitigasi pemilihan program studi.
- **Bebas Ketergantungan Eksternal Berat:** Dijalankan secara mandiri dengan performa tinggi.

---

## English

### 1. Overview & Educational Context
Every academic cycle, hundreds of thousands of prospective students across Indonesia navigate admissions for top public universities (PTN) via national tracks (SNBP achievement track and SNBT computer-based entrance examination) as well as premier private institutions (PTS) via their respective entrance mechanisms.

Information asymmetry often leads students to select poorly calibrated choice pairs (such as placing two ultra-selective programs in both slots or omitting safety nets), resulting in unnecessary rejection across both options. This platform bridges that gap by providing transparent, structured analytics on university selectivity ratios, historical applicant trajectories, and portfolio risk calibration across 50 top universities (35 PTN & 15 PTS) spanning 5 major Indonesian island regions.

---

### 2. Mathematical Methodology

Selectivity is modeled using two standard quantitative metrics:

#### A. Selectivity Rate (Percentage)
$$\text{Selectivity Rate} = \left( \frac{\text{Quota (Daya Tampung)}}{\text{Applicants (Peminat)}} \right) \times 100\%$$
*A lower percentage indicates a more selective and fiercely contested academic program.*

Classification Thresholds:
- **Very Competitive:** $< 2.50\%$ (National peak competition, applicant-to-quota ratio $> 1 : 40$).
- **Competitive:** $2.50\% - 5.00\%$ (High competition, ratio between $1 : 20$ and $1 : 40$).
- **Moderate:** $5.01\% - 10.00\%$ (Balanced competition, ratio between $1 : 10$ and $1 : 20$).
- **Open / Accessible:** $> 10.00\%$ (More accessible, ratio $< 1 : 10$).

#### B. Competition Ratio
$$\text{Competition Ratio} = 1 : \left\lceil \frac{\text{Applicants}}{\text{Quota}} \right\rceil$$
*Example:* A $1 : 55$ ratio implies that 55 applicants compete for a single available seat.

---

### 3. Nationwide Institutional Scope

The dataset covers 50 accredited top higher education institutions across 5 geographical zones:
- **Java (Jawa):** 21 PTN (UI, ITB, UGM, IPB, UNAIR, ITS, UNDIP, UB, UNPAD, UNS, UPI, UNSOED, UNY, UNNES, UNESA, UM, UNJ, UPNVJ, UPNVYK, UPNVJT, UNTIRTA) and 15 PTS (Telkom University, Binus University, UII, UMY, UNPAR, Atma Jaya, UPH, Trisakti, Untar, UMN, Petra Christian University, UMS, President University, Sanata Dharma, Mercu Buana).
- **Sumatra:** 7 PTN (USU, UNAND, UNSRI, UNILA, UNP, USK, UNRI).
- **Kalimantan:** 3 PTN (UNMUL, ULM, UNTAN).
- **Sulawesi:** 2 PTN (UNHAS, UNSRAT).
- **Bali & Nusa Tenggara:** 2 PTN (UNUD, UNRAM).

---

### 4. Key Platform Capabilities

- **National Selectivity Leaderboard:** Top 50 most competitive academic programs nationwide, filterable by admission track (SNBT vs SNBP), scientific cluster (Science & Technology vs Social Sciences & Humanities), institution type (All, PTN Only, PTS Only), and geographical region.
- **Multi-Campus Head-to-Head Comparison:** Direct cross-university evaluation of equivalent majors across all 50 public and private universities.
- **Choice Portfolio Risk Simulator:** Intelligent heuristic algorithm that evaluates two-choice applications to detect inverted selectivity orders, over-concentration of risk, and hybrid PTN-PTS safety net strategies.
- **Searchable Directory & Historical Breakdown:** Interactive program lookup with 3-year applicant trend graphs (2022-2024), curriculum focuses, career outlooks, and direct links to official SPMB admission portals.
- **Full Bilingual Support:** Real-time localization between Indonesian and English with synchronized URL parameters (`?lang=en` or `?lang=id`).
- **Open Data Distribution:** Machine-readable datasets exported in JSON and CSV for researchers, educators, and prospective applicants.

---

### 5. Editorial UI Design & Visual Data-Journalism Architecture

The interactive platform (`index.html`) implements institutional data-journalism design standards:
- **Obsidian & Sovereign Indigo Palette:** Combines deep dark obsidian tones (`#0a1128`, `#001f54`) in the masthead and hero with a crisp warm alabaster canvas (`#f8fafc`) and hairline borders (`#e2e8f0`).
- **Dual-Engine Typography:** Utilizes `Plus Jakarta Sans` for editorial typography and `JetBrains Mono` (`font-variant-numeric: tabular-nums`) for tabular number alignment across quotas, applicants, and percentages.
- **Rank Medallions & Inline Competition Density Meters:** Top 3 leaderboard entries feature gold, silver, and bronze medallions. Competition ratios (1 : N) feature dynamic horizontal density progress bars.
- **Intelligent Strategy Assessment Card:** Portfolio simulation outcomes are delivered with colored status accents, risk level gauges, and actionable strategic advice.
- **Zero Heavy Dependencies:** Clean, standalone runtime without external framework overhead.

---

### 6. Data Citation & License

- **Data Attribution:** Compiled from official figures released by the National Selection Committee for Higher Education (Balai Pengelolaan Pengujian Pendidikan / BPPP SNPMB, Ministry of Education, Culture, Research, and Technology) and official admissions portals of all 50 featured institutions.
- **License:** Open educational and public research use. Free to inspect, analyze, and build upon.
