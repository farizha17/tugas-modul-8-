# Tugas 4 Rekayasa Perangkat Lunak

**Nama:** Farizha Isnaini  
**Mata Kuliah:** Rekayasa Perangkat Lunak  
**Proyek:** Pengelolaan Data Buku dan Anggota Perpustakaan

## Deskripsi
Proyek ini merupakan implementasi pengelolaan data buku dan anggota perpustakaan menggunakan Python dan MySQL.

## Fitur
### 1. Pengelolaan Buku
- Menampilkan data buku.
- Mengubah data buku menggunakan metode `update_buku()`.
- Menghapus data buku menggunakan metode `delete_buku()`.

### 2. Pengelolaan Anggota
- Menambahkan data anggota menggunakan metode `tambah_anggota()`.
- Menampilkan data anggota menggunakan metode `tampil_anggota()`.

## Teknologi
- Python
- MySQL
- MySQL Connector/Python
- Visual Studio Code
- Laragon

## Struktur Proyek
```text
Tugas_4_RPL_F5212520078/
├── models/
│   ├── __init__.py
│   ├── database.py
│   ├── buku_model.py
│   └── anggota_model.py
├── tests/
│   └── test_model.py
├── .gitignore
└── README.md
```

## Database
Nama database: `perpustakaan`

Tabel yang digunakan:
- `buku`
- `anggota`

## Pengujian
Pengujian dilakukan menggunakan modul `unittest` Python.

Perintah pengujian:

```bash
python -m unittest tests.test_model -v
```

Hasil pengujian: seluruh pengujian berhasil dijalankan.