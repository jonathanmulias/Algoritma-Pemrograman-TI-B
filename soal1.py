"""
1.1 Soal 1 (Function dan Validasi Data)
Buat sebuah fungsi bernama rata rata(nilai) yang:
1. Menerima sebuah list berisi nilai mahasiswa
2. Menghitung rata-rata nilai
3. Jika list kosong, kembalikan pesan: "Data kosong"
Kemudian:
1. Panggil fungsi dengan list: [80, 75, 90, 60, 85]
2. Tampilkan hasilnya

"""

rata_rata_nilai = [80, 75, 90, 60, 85]

if len(rata_rata_nilai) > 0:
    rata_rata_nilai = sum(rata_rata_nilai) / len(rata_rata_nilai)
    print(rata_rata_nilai)
else:
    print("Data kosong") 