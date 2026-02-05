"""
Buat sebuah fungsi bernama hitung(a, b) yang:
1. Menerima dua parameter a dan b
2. Mengembalikan hasil penjumlahan a + b
3. Mengembalikan hasil pengurangan a - b
Kemudian:
1. Panggil fungsi tersebut
2. Tampilkan hasil penjumlahan dan pengurangannya ke layar
Contoh keluaran:
Penjumlahan = 8
Pengurangan = 2

"""

def my_function(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan

proses_penambahan, proses_pengurangan = my_function(5, 3)

print("Penjumlahan =", proses_penambahan)
print("Penjumlahan =", proses_pengurangan)