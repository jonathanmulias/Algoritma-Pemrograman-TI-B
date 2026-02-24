"""
1.4 Soal 4 (Perulangan)
Buat sebuah program Python yang:
1. Menggunakan perulangan for
2. Menampilkan bilangan dari 1 sampai 10
3. Menghitung dan menampilkan jumlah dari bilangan 1 sampai 10
Contoh keluaran:
1
2
3
4
5
6
7
8
9
10
Jumlah = 55

"""

#CARA 1

jumlah = 0

for i in range(1, 11):
    jumlah += i

print("Jumlah =", jumlah)


#CARA 2 (TAMBAHAN)

jumlah = 0

for i in range(1, 11):
    jumlah += i

print(f"Jumlah = {jumlah}")