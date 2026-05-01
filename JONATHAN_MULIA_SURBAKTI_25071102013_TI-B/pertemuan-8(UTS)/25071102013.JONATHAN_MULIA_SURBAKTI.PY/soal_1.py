DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

def tebak_angka(angka_rahasia, maks_percobaan):
    for maks_percobaan in range(7):
        angka = int(input("Masukkan angka tebakan mu : "))
        if angka <= angka_rahasia:
            print("Terlalu kecil")
        elif angka >= angka_rahasia:
            print("Terlalu besar")
        elif angka == angka_rahasia:
            return True
        elif maks_percobaan == 0:
            return False

def hitung_skor(angka, skor):
    skor = 0
    if angka == True:
        print("Benar")
        skor += 10
    elif angka == False:
        skor = 0

def main_satu_ronde(hasil, menghitung_skor):
    angka_rahasia = 89
    hasil = tebak_angka(angka_rahasia, 7)
    menghitung_skor = hitung_skor(3, 10)

    print(hasil)
    print(menghitung_skor)

permainan = main_satu_ronde(hasil, menghitung_skor)

print(permainan)