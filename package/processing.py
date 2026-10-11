#Class untuk satu pengeluaran
class Pengeluaran:
    def __init__(self, tanggal, keterangan, jumlah):
        self.tanggal = tanggal
        self.keterangan = keterangan
        self.jumlah = jumlah

    def info(self):
        return f"{self.tanggal} | {self.keterangan} | Rp{self.jumlah:,}"

#Class untuk mengelola kumpulan pengeluaran
class BukuKas:
    def __init__(self):
        self.data = []

    #Menambahkan satu pengeluaran ke dalam buku kas
    def tambah(self, pengeluaran):
        self.data.append(pengeluaran)

    #Menghitung total semua pengeluaran
    def total(self):
        return sum(p.jumlah for p in self.data)

    #Menghitung rata-rata pengeluaran
    def rata(self):
        return self.total() / len(self.data) if self.data else 0

    #Mencari pengeluaran terbesar
    def terbesar(self):
        return max(self.data, key=lambda p: p.jumlah) if self.data else None

    #Mengurutkan pengeluaran terbesar
    def urut(self):
        return sorted(self.data, key=lambda p: p.jumlah, reverse=True)


#Menghitung total dari sejumlah nilai
def total(*args):
    return sum(args)


#Membuat ringkasan analisis dari list of dictionary
def ringkasan(data):
    if not data:
        return "Tidak ada data."
    semua_jumlah = [d['jumlah'] for d in data]
    total_semua = total(*semua_jumlah)
    return (
        f"Total : Rp{total_semua:,}\n"
        f"Rata-rata : Rp{total_semua / len(data):,.0f}\n"
        f"Terbesar : {max(data, key=lambda d: d['jumlah'])['keterangan']}\n"
    )