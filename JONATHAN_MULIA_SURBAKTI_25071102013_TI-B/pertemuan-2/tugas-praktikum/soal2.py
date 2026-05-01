"""
1.2 Soal 2 (Range dan Pola Bilangan)
Buat sebuah fungsi bernama bilangan prima(n) yang:
1. Menggunakan range()
2. Mengembalikan list bilangan prima dari 1 sampai n
Kemudian:
1. Panggil fungsi untuk n = 50
2. Tampilkan hasilnya

"""

def bilangan_prima(n):
    hasil = []
    for nilai in range(2, n + 1):
        is_prima = True
        for i in range(2, nilai):
            if nilai % i == 0:
                is_prima = False
                break
        if is_prima:
            hasil.append(nilai)
    return hasil

data_prima = bilangan_prima(50)

for angka in data_prima:
    print(angka)