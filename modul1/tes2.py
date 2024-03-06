def katakan(bilangan):
    if bilangan == 0:
        return "Nol"
    elif bilangan > 999999999999 :
      return "Angka terlalu besar"
    
    satuan = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan"]
    belasan = ["", "Sebelas", "Dua Belas", "Tiga Belas", "Empat Belas", "Lima Belas", "Enam Belas", "Tujuh Belas", "Delapan Belas", "Sembilan Belas"]
    puluhan = [" ", "Sepuluh ", "Dua Puluh ", "Tiga Puluh ", "Empat Puluh ", "Lima Puluh ", "Enam Puluh ", "Tujuh Puluh ", "Delapan Puluh ", "Sembilan Puluh "]

    def konversi_triple(angka):
        result = ""

        if angka // 100 > 0:
            result += satuan[angka // 100] + " Ratus "

        angka %= 100

        if angka // 10 == 1:
            result += belasan[angka % 10]
        else:
            result += puluhan[angka // 10] + satuan[angka % 10]

        return result

    miliar = bilangan // 1000000000
    juta = (bilangan % 1000000000) // 1000000
    ribu = (bilangan % 1000000) // 1000
    sisa = bilangan % 1000

    result = ""

    if miliar > 0:
        result += konversi_triple(miliar) + " Miliar "

    if juta > 0:
        result += konversi_triple(juta) + " Juta "

    if ribu > 0:
        result += konversi_triple(ribu) + " Ribu "

    result += konversi_triple(sisa)
    
    result = result.replace("Satu Ratus","Seratus")

    return result.strip()

print(katakan(3125150))
print(katakan(9999999999999))