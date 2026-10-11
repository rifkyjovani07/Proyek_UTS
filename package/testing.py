import unittest
from package.processing import BukuKas, Pengeluaran, total, ringkasan
from package.validasi import cek_jumlah


class TestPengeluaran(unittest.TestCase):
    def setUp(self):
        #Contoh data yang dipakai untuk semua test/pengujian
        self.data = [
            {"tanggal": "2026-01-01", "keterangan": "Makan", "jumlah": 25000},
            {"tanggal": "2026-01-02", "keterangan": "Belanja", "jumlah": 100000},
            {"tanggal": "2026-01-03", "keterangan": "Kopi", "jumlah": 18000},
        ]
        self.kas = BukuKas()
        self.kas.tambah(Pengeluaran("2026-01-01", "Makan", 25000))
        self.kas.tambah(Pengeluaran("2026-01-02", "Belanja", 100000))
        self.kas.tambah(Pengeluaran("2026-01-03", "Kopi", 18000))

    def test_total(self):
        # Cek total: 25000 + 100000 + 18000 = 143000
        self.assertEqual(total(25000, 100000, 18000), 143000)

    def test_bukukas_total(self):
        # Cek total dari BukuKas = 143000
        self.assertEqual(self.kas.total(), 143000)

    def test_bukukas_rata(self):
        # Cek rata-rata = 143000 dibagi 3
        self.assertEqual(self.kas.rata(), 143000 / 3)

    def test_bukukas_terbesar(self):
        # Cek pengeluaran terbesar = Belanja
        self.assertEqual(self.kas.terbesar().keterangan, "Belanja")

    def test_bukukas_urut(self):
        # Cek urutan pertama = Belanja karena paling besar
        hasil = self.kas.urut()
        self.assertEqual(hasil[0].keterangan, "Belanja")

    def test_validasi(self):
        # Cek kalau jumlah negatif, harus muncul error
        with self.assertRaises(ValueError):
            cek_jumlah(-100)


if __name__ == '__main__':
    unittest.main()