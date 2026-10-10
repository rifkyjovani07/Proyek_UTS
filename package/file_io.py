#Buat file untuk pertama kali
def buat_file(nama):
    try:
        with open(nama, "x") as f:
            f.write("2026-01-01;Makan;25000\n")
    except FileExistsError:
        print(f"File '{nama}' sudah ada.")


#Menambah data
def tambah(nama, **data):
    with open(nama, "a") as f:
        f.write(f"{data['tanggal']};{data['ket']};{data['jumlah']}\n")

#Membaca file
def baca(nama):
    hasil = []
    try:
        with open(nama, "r") as f:
            for baris in f:
                try:
                    tgl, ket, jml = baris.strip().split(";")
                    hasil.append({"tanggal": tgl, "ket": ket, "jumlah": int(jml)})
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"File '{nama}' tidak ada.")
    return hasil

#Buat laporan
def tulis_laporan(nama, isi):
    with open(nama, "w") as f:
        f.write(isi)


if __name__ == '__main__':
    buat_file("data.txt")