class Pengeluaran:
    # Class untuk satu pengeluaran
    def __init__(self, tanggal, keterangan, jumlah):
        self.tanggal = tanggal
        self.keterangan = keterangan
        self.jumlah = jumlah

    def info(self):
        # Tampilkan info pengeluaran
        return f"{self.tanggal} | {self.keterangan} | Rp{self.jumlah:,}"


class BukuKas:
    # Class untuk mengelola kumpulan pengeluaran
    def __init__(self):
        self.data = []

    def tambah(self, pengeluaran):
        self.data.append(pengeluaran)

    def total(self):
        return sum(p.jumlah for p in self.data)

    def rata(self):
        if not self.data:
            return 0
        
        return self.total() / len(self.data)

    def terbesar(self):
        return max(self.data, key=lambda p: p.jumlah)

    def urut(self):
        return sorted(self.data, key=lambda p: p.jumlah, reverse=True)


def total(*args):
    return sum(args)


def ringkasan(data):
    if not data:
        return "Tidak ada data."
    semua_jumlah = [d["jumlah"] for d in data]
    total_semua = total(*semua_jumlah)
    return (
        f"Total : Rp{total_semua:,}\n"
        f"Rata-rata : Rp{total_semua / len(data):,.0f}\n"
        f"Terbesar : {max(data, key=lambda d: d['jumlah'])['keterangan']}\n"
    )