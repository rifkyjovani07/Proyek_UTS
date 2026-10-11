#Memastikan bahawa jumlah adalah angka positif
def cek_jumlah(jumlah):
    assert isinstance(jumlah, int), "Jumlah harus int"

    if jumlah < 0:
        raise ValueError("Jumlah tidak boleh negatif.")
    
    return jumlah

#Memastikam field tidak kosong
def cek_field(teks):
        if not teks or not teks.strip():
              raise ValueError("Field tidak boleh kosong.")
        return True