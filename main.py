from package import fileio, processing, validasi

FILE = "data.txt"
LAPORAN = "laporan.txt"


def main():
    # Buat file untuk pertama kali
    fileio.buat_file(FILE)

    # Tambah data
    try:
        validasi.cek_jumlah(18000)
        validasi.cek_field("Kopi")
        fileio.tambah(FILE, tanggal="2026-01-04", ket="Kopi", jumlah=18000)
    except ValueError as e:
        print(f"Gagal: {e}")

    #Membaca data
    data = fileio.baca(FILE)

    #Memasukkan data ke BukuKas
    kas = processing.BukuKas()
    for d in data:
        kas.tambah(processing.Pengeluaran(d["tanggal"], d["ket"], d["jumlah"]))

    #Menampilkan data
    print("Semua data:")
    for p in kas.data:
        print("  " + p.info())

    print()
    print(f"Total : Rp{kas.total():,}")
    print(f"Rata-rata : Rp{kas.rata():,.0f}")
    print(f"Terbesar : {kas.terbesar().info()}")

    print("\nUrut dari terbesar:")
    for p in kas.urut():
        print("  " + p.info())

    #Tulis laporan
    fileio.tulis_laporan(LAPORAN, processing.ringkasan(data))
    print(f"\nLaporan ditulis ke '{LAPORAN}'.")


if __name__ == '__main__':
    main()