def katakan(angka):
    # Daftar string untuk nilai tempat
    satuan = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
    belasan = ["", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
    puluhan = ["", "", "dua puluh", "tiga puluh", "empat puluh", "lima puluh", "enam puluh", "tujuh puluh", "delapan puluh", "sembilan puluh"]
    
    # Fungsi rekursi untuk menangani bilangan lebih besar dari 999
    def rekursi(angka, trilyun=False):
        if angka < 1_000_000_000:
            if angka < 1_000_000:
                if angka < 1_000:
                    return tiga_digit(angka)
                else:
                    ribuan = angka // 1_000
                    return tiga_digit(ribuan) + " ribu" + (" " + rekursi(angka % 1_000) if angka % 1_000 else "")
            else:
                jutaan = angka // 1_000_000
                return tiga_digit(jutaan) + " juta" + (" " + rekursi(angka % 1_000_000) if angka % 1_000_000 else "")
        else:
            return "Angka terlalu besar"
    
    # Fungsi untuk menangani bilangan di bawah 1000
    def tiga_digit(angka):
        if angka < 100:
            if angka < 20:
                return belasan[angka] if angka > 10 else satuan[angka]
            else:
                return puluhan[angka // 10] + (" " + satuan[angka % 10] if angka % 10 else "")
        else:
            ratusan = angka // 100
            return satuan[ratusan] + " ratus" + (" " + tiga_digit(angka % 100) if angka % 100 else "")
    
    # Mengecek batasan input
    if angka < 0 or angka >= 1_000_000_000:
        return "Angka di luar batas"
    else:
        return rekursi(angka)

# Contoh penggunaan
print(katakan(3125750))  # Output: tiga juta seratus dua puluh lima ribu tujuh ratus lima puluh
print(katakan(21))  # Output: dua puluh satu
print(katakan(1000000000))  # Output: Angka di luar batas