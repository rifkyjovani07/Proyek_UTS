# Proyek UTS - Catatan Pengeluaran Harian

Program Python sederhana untuk mencatat dan menganalisis pengeluaran harian. Dibuat untuk memenuhi Ujian Tengah Semester (UTS) mata kuliah Pemrograman Terstruktur.

## Deskripsi

Program ini membaca data pengeluaran dari file `data.txt`, menganalisis total, rata-rata, dan pengeluaran terbesar, lalu menuliskan laporan ke `laporan.txt`. Program juga dilengkapi dengan pengujian otomatis menggunakan `unittest`.

## Struktur Folder
Proyek_UTS/
├── main.py 
├── data.txt 
├── laporan.txt
└── package/
├── init.py 
├── fileio.py 
├── processing.py 
├── validasi.py 
└── testing.py 

## Fitur

- Membaca data pengeluaran dari file (`mode r`)
- Menambahkan pengeluaran baru (`mode a`)
- Membuat file data pertama kali (`mode x`)
- Menulis laporan ke file (`mode w`)
- 2 class: `Pengeluaran` dan `BukuKas`
- 5+ fungsi analisis
- Penggunaan `*args`, `**kwargs`, `lambda`, keyword argument
- `try/except`, `raise`, `assert`
- 6 unit test dengan `unittest`
