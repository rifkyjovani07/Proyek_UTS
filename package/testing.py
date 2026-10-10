import unittest
from package.processing import BukuKas, Pengeluaran, total, ringkasan
from package.validasi import cek_jumlah


class TestPengeluaran(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"tanggal": "2026-01-01", "ket": "Makan", "jumlah": 25000},
            {"tanggal": "2026-01-02", "ket": "Belanja", "jumlah": 100000},
            {"tanggal": "2026-01-03", "ket": "Kopi", "jumlah": 18000},
        ]
        self.kas = BukuKas()
        self.kas.tambah(Pengeluaran("2026-01-01", "Makan", 25000))
        self.kas.tambah(Pengeluaran("2026-01-02", "Belanja", 100000))
        self.kas.tambah(Pengeluaran("2026-01-03", "Kopi", 18000))

    def test_total(self):
        self.assertEqual(total(25000, 100000, 18000), 143000)

    def test_bukukas_total(self):
        self.assertEqual(self.kas.total(), 143000)

    def test_bukukas_rata(self):
        self.assertEqual(self.kas.rata(), 143000 / 3)

    def test_bukukas_terbesar(self):
        self.assertEqual(self.kas.terbesar().ket, "Belanja")

    def test_bukukas_urut(self):
        hasil = self.kas.urut()
        self.assertEqual(hasil[0].ket, "Belanja")

    def test_validasi(self):
        with self.assertRaises(ValueError):
            cek_jumlah(-100)


if __name__ == '__main__':
    unittest.main()