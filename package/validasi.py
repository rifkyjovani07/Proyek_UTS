def cek_jumlah(jumlah):
    if jumlah < 0:
        raise ValueError("Jumlah tidak boleh negatif.")
    assert isinstance(jumlah, int), "Jumlah harus int"
    return True


def cek_field(teks):
        if not teks or not teks.strip():
              raise ValueError("Field tidak boleh kosong.")
        return True