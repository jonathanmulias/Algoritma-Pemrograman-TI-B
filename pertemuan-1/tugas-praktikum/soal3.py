"""
Buat sebuah program Python yang:
1. Menyimpan sebuah nilai ujian (0-100) ke dalam variabel
2. Jika nilai lebih besar atau sama dengan 60, tampilkan:
Lulus
Jika nilai kurang dari 60, tampilkan:
Tidak Lulus

"""

#CARA 1

nilai_ujian = 85

if nilai_ujian >= 60:
    print("lulus")
else:
    print("Tidak lulus")


#CARA 2 (TAMBAHAN)

nilai_ujian = 85

if nilai_ujian >= 60:
    print("lulus")
elif nilai_ujian <= 60:
    print("Tidak lulus")