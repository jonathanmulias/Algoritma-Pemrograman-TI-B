"""
1.5 Soal 5 (Python Module dan Algoritma)
Buat sebuah program Python yang:
1. Menggunakan module math
2. Membuat fungsi jarak(x1, y1, x2, y2) untuk menghitung jarak dua titik pada
bidang Kartesius
3. Menggunakan rumus:
d =
p
(x2 - x1)2 + (y2 - y1)2

Contoh keluaran:
Jarak = 5.0

"""
import math

def jarak(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Jarak =", jarak(1, 1, 4, 5))

