# Definisi Matematis & Panduan Formula Keketatan Program Studi

Dalam sistem seleksi penerimaan mahasiswa baru di Indonesia (SNBP, SNBT, dan Seleksi Mandiri), istilah **keketatan** dan **rasio persaingan** digunakan sebagai indikator kuantitatif utama untuk mengukur tingkat kompetisi suatu program studi.

---

## 1. Persentase Keketatan (Selectivity Percentage)

Persentase keketatan mengukur proporsi calon mahasiswa yang berhasil diterima dibandingkan dengan total pendaftar yang memilih program studi tersebut.

### Formula Matematis

$$\text{Keketatan} (\%) = \left( \frac{\text{Daya Tampung}}{\text{Peminat}} \right) \times 100\%$$

Di mana:
- **Daya Tampung ($D$):** Jumlah kursi atau kapasitas maksimal mahasiswa baru yang dialokasikan oleh universitas untuk program studi pada jalur seleksi tertentu.
- **Peminat ($P$):** Jumlah total pendaftar yang mencantumkan program studi tersebut sebagai pilihan seleksi pada periode tahun sebelumnya.

### Karakteristik Matematis:
- **Hubungan Berbanding Terbalik:** Semakin **kecil** persentase keketatan, semakin **ketat** dan sulit persaingan masuk ke program studi tersebut.
- Nilai dibulatkan ke dua angka di belakang koma (contoh: 1,24%, 3,50%).

---

## 2. Rasio Persaingan (Competition Ratio)

Rasio persaingan merepresentasikan peluang satu orang pendaftar dibandingkan dengan total kandidat yang bersaing memperebutkan satu kursi.

### Formula Matematis

$$\text{Rasio} = 1 : N \quad \text{dengan} \quad N = \text{round}\left( \frac{\text{Peminat}}{\text{Daya Tampung}} \right)$$

Di mana:
- Angka $1$ merepresentasikan 1 kursi yang tersedia.
- Angka $N$ merepresentasikan estimasi jumlah pendaftar yang bersaing untuk memperebutkan 1 kursi tersebut.

---

## 3. Matriks Interpretasi Tingkat Kompetisi

Berdasarkan analisis statistik seleksi nasional di 50 universitas terkemuka di Indonesia:

| Kategori Keketatan | Rentang Persentase | Estimasi Rasio | Karakteristik Program Studi |
|---|---|---|---|
| **Hyper-Competitive** | $< 2,00\%$ | $> 1 : 50$ | Pendidikan Dokter, Ilmu Komputer/Informatika, Manajemen, Ilmu Komunikasi di PTN Klaster 1 |
| **Highly Competitive** | $2,00\% - 5,00\%$ | $1 : 20 - 1 : 50$ | Farmasi, Psikologi, Teknik Sipil, Teknik Industri, Akuntansi, Ilmu Hukum |
| **Competitive** | $5,00\% - 10,00\%$ | $1 : 10 - 1 : 20$ | Sains Dasar (Matematika, Kimia), Sastra, Arsitektur, Agribisnis |
| **Moderate** | $> 10,00\%$ | $< 1 : 10$ | Program studi vokasi spesifik, program studi baru, atau kampus wilayah luar Jawa |

---

## 4. Contoh Komputasi Kasus Nyata

Sebagai ilustrasi komputasi pada seleksi SNBT:
- Program Studi: **S1 Kedokteran**
- Daya Tampung: $50$ kursi
- Peminat Tahun Sebelumnya: $3.850$ peserta

Perhitungan:
1. **Persentase Keketatan:**
   $$\text{Keketatan} = \left( \frac{50}{3850} \right) \times 100\% = 1,2987\% \approx 1,30\%$$
2. **Rasio Persaingan:**
   $$N = \text{round}\left( \frac{3850}{50} \right) = 77 \implies 1 : 77$$

Artinya, setiap 1 kursi yang diperebutkan diperebutkan oleh sekitar 77 peserta ujian, menempatkannya pada kategori **Hyper-Competitive**.
