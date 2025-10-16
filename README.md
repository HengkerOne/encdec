# PROFESSIONAL CODE ENCRYPTOR 🔒



**Alat enkripsi kode Python tingkat profesional yang kuat, dirancang untuk melindungi kode sumber Anda dari analisis dan modifikasi yang tidak sah.**

Aplikasi ini menggabungkan beberapa algoritma kriptografi dan teknik *obfuscation* terdepan untuk menghasilkan *runtime loader* Python (`.py`) yang terlindungi.

***

## 🌟 Fitur Utama

* **Enkripsi Kode Sumber yang Kuat:** Konten utama kode Anda dienkripsi menggunakan **Fernet (AES-128-bit) yang teruji di industri.**
* **Penurunan Kunci Aman:** Memanfaatkan **PBKDF2-HMAC** untuk menurunkan kunci enkripsi yang sangat kuat dari *passphrase* atau kata sandi, memastikan kerahasiaan kunci maksimum.
* **Verifikasi Integritas Data:** Menggunakan **HMAC-SHA256** untuk memverifikasi bahwa kode yang dienkripsi belum dirusak atau dimodifikasi selama transit atau penyimpanan.
* ***Obfuscation* Tingkat Lanjut:** Menggabungkan teknik **Marshal dan XOR** untuk kompilasi *bytecode* dan *obfuscation* tambahan, membuat rekayasa balik menjadi jauh lebih sulit.
* **Output yang Siap Digunakan:** Menghasilkan *runtime loader* Python (`.py`) yang **sepenuhnya berfungsi dan terlindungi** yang dapat langsung digunakan oleh pengguna Anda.

***

## 📸 Tampilan (Screenshots)

Untuk melihat alat ini beraksi, silakan lihat tangkapan layar berikut.

| Deskripsi | Tangkapan Layar |
| :--- | :---: |
| **Proses Enkripsi** | [![Proses Enkripsi](https://raw.githubusercontent.com/HengkerOne/encdec/refs/heads/main/Screenshot_20251016-213922.jpg)](screenshots/encrypt_process.png) |
| **File *Loader* yang Dihasilkan** | [![File Output Loader]([screenshots/output_files.png](https://raw.githubusercontent.com/HengkerOne/encdec/refs/heads/main/Screenshot_20251016-215535.jpg))]([screenshots/output_files.png](https://raw.githubusercontent.com/HengkerOne/encdec/refs/heads/main/Screenshot_20251016-215535.jpg)) |
| **Pengujian *Decryption* & Eksekusi** | [![Eksekusi Loader](screenshots/loader_execution.png)](screenshots/loader_execution.png) |

*Pastikan Anda telah membuat folder **`screenshots/`** di repositori Anda dan menempatkan file gambar dengan nama yang sesuai: `encrypt_process.png`, `output_files.png`, dan `loader_execution.png`.*

***

## ⚙️ Cara Kerja

Alat ini bekerja dalam beberapa langkah untuk memastikan keamanan berlapis pada kode Anda:

1.  **Pemuatan Kode:** Kode sumber Anda dimuat dan disiapkan.
2.  **Penurunan Kunci:** Kunci enkripsi kuat dihasilkan menggunakan **PBKDF2-HMAC** dari *salt* dan kata sandi yang Anda berikan.
3.  **Enkripsi Inti:** Konten utama kode dienkripsi menggunakan **Fernet (AES-128-bit)**.
4.  **Integritas Data:** Sebuah *hash* **HMAC-SHA256** dibuat dari konten terenkripsi untuk memverifikasi integritas.
5.  ***Obfuscation* (Opsional):** Bytecode dikompilasi dan di-*obfuscate* lebih lanjut menggunakan Marshal/XOR.
6.  **Pembuatan Loader:** Semua komponen (*salt*, *hash*, data terenkripsi, dan logika *decryption/loading*) dikemas menjadi satu file *runtime loader* Python (`.py`).

***

## 🚀 Instalasi

### Prasyarat

* Python 3.x

### Langkah-langkah Instalasi

Clone repositori ini:

```bash
git clone [https://github.com/HengkerOne/encdec.git](https://github.com/HengkerOne/HengkerOne/encdec.git)
cd encdec
