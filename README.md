# Sistem Login & Registrasi Sederhana dengan PyQt6

Proyek ini adalah aplikasi berbasis GUI sederhana yang menggunakan Python dan PyQt6 untuk membuat sistem login dan registrasi yang ramah pengguna. Kredensial pengguna disimpan dengan aman dalam database lokal SQLite. Setelah login berhasil, pengguna akan diarahkan ke menu utama dengan opsi untuk logout.

## Fitur
- Login: Pengguna dapat masuk dengan username dan password.
- Registrasi: Pengguna baru dapat membuat akun dengan username dan password unik.
- Tampilkan/Sembunyikan Password: Fitur untuk menampilkan atau menyembunyikan password di form login dan registrasi.
- Bersihkan Input: Field username dan password akan otomatis kosong setelah login atau registrasi berhasil.
- Menu Utama dengan Logout: Setelah login, pengguna akan diarahkan ke menu utama dan dapat logout untuk kembali ke layar login.

## Instalasi

1. Pastikan Anda telah menginstal Python (versi 3 atau lebih baru) di komputer Anda. Jika belum, Anda bisa mengunduhnya di [python.org](https://www.python.org/downloads/).

2. Clone repositori ini atau salin file Python yang disertakan.

```bash
git clone https://github.com/Zetakai/SimpleQtLogin.git
```
3. Masuk ke direktori proyek dan buat virtual environment (venv) menggunakan perintah:

```bash
cd SimpleQtLogin
python -m venv env
```

4. Aktifkan virtual environment:

- Windows:
```bash
env/Scripts/Activate.ps1
```
- Linux/MacOS:
```bash
source env/bin/activate
```

5. Instal semua dependensi yang diperlukan dari file requirements.txt:

```bash
pip install -r requirements.txt
```
6. Jalankan program menggunakan Python:
   
```bash
python app.py
```

## Persyaratan
- Python 3.x
- PyQt6

## Struktur Proyek

```bash
SimpleQtLogin/
│
├── app.py                # File utama yang berisi kode program
├── README.md             # Dokumentasi ini
├── requirements.txt      # Daftar dependensi yang diperlukan
├── env/                  # Virtual environment (tidak perlu diupload ke repositori)
├── users.db              # Sqlite database berisi informasi users
```

## Menggunakan Virtual Environment (venv) dan requirements.txt
Aplikasi ini menggunakan virtual environment (venv) untuk mengisolasi dependensi dan paket Python serta file requirements.txt untuk mempermudah instalasi dependensi. Berikut adalah cara menggunakannya:

1. Buat virtual environment dengan perintah:

```bash
python -m venv env
```
2.  Aktifkan virtual environment:
- Windows:
```bash
env/Scripts/Activate.ps1
```
- Linux/MacOS:
```bash
source env/bin/activate
```
3.  Instal semua dependensi yang terdaftar di requirements.txt:
```bash
pip install -r requirements.txt
```
4.  Untuk menonaktifkan virtual environment, jalankan perintah:
```bash
deactivate
```

## Kontribusi
Jika Anda ingin berkontribusi dalam pengembangan aplikasi ini, Anda dipersilakan untuk membuat pull request atau mengirimkan issue.

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Silakan lihat file LICENSE untuk detailnya.

```markdown

### Penjelasan Tambahan:
1. **Instalasi dengan `requirements.txt`**: Langkah instalasi diperbarui untuk memasukkan penggunaan `requirements.txt` agar pengguna dapat menginstal semua dependensi sekaligus.
2. **Virtual Environment dan `requirements.txt`**: Bagian ini menjelaskan bagaimana mengisolasi proyek dan mengelola dependensi menggunakan virtual environment serta file `requirements.txt`.

Anda bisa menambahkan dependensi ke dalam file `requirements.txt` sesuai dengan kebutuhan proyek Anda.
```
