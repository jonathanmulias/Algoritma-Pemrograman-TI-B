#P Y T H O N   S Y N T A X
#1. || SYNTAX ||
    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPILAN RAPIH

print("-------------------------------------------------------------------------------------------------")

    #A. SYNTAX
        
        #CARA MENAMPILKAN "Hello World!" DI PYTHON

print("Hello World!") #CARA 1 MENGGUNAKAN DOUBLE QUOTE (PETIK DUA)

print("-------------------------------------------------------------------------------------------------")

print('Hello World!') #CARA 2 MENGGUNAKAN SINGLE QUOTE (PETIK SATU)

print("-------------------------------------------------------------------------------------------------")

    #B. INDENTATION
        #INDENTASI MENGACU PADA SPASI DI AWAL BARIS KODE
        #DI DALAM PYTHON INDENTASI SANGAT PENTING

if 6 > 3:                                       #CONTOH
    print("Enam lebih besar dari tiga!")        #BENAR

print("-------------------------------------------------------------------------------------------------")

"""
if 6 > 3:                                       CONTOH
print("Enam lebih besar dari tiga!")            SALAH

"""
        #HARUS MENGGUNAKAN JUMLAH SPASI YANG SAMA DALAM BLOK KODE YANG SAMA
        #KALAU TIDAK, PYTHON AKAN MEMBERIKAN KESALAHAN

if 7 > 2:                                       #CONTOH
    print("Tujuh lebih besar dari dua!")        #BENAR
    print("Tujuh lebih besar dari dua!")

print("-------------------------------------------------------------------------------------------------")

"""
if 7 > 2:                                       CONTOH
 print("Tujuh lebih besar dari dua!")           SALAH
        print("Tujuh lebih besar dari dua!")

"""

#2. || STATEMENTS ||
    #TIDAK PERLU MENGGUNAKAN TITIK KOMA (;) UNTUK MENGAKHIRI SEBUAH PERNYATAAN

    #CARA 1

print("Halo")
print("Apa kabar?")
print("Nama ku Jonathan")

print("-------------------------------------------------------------------------------------------------")

    #CARA 2
    #DIGUNAKAN UNTUK MENULIS BEBERAPA PERNYATAAN DALAM SATU BARIS DENGAN MEMISAHKANNYA 
    #MENGGUNAKAN TANDA TITIK KOMA (;) 

print("Halo"); print("Apa kabar?"); print("Nama ku Jonathan")

print("-------------------------------------------------------------------------------------------------")

    #CARA SALAH
    #JIKA MELETAKKAN DUA PERNYATAAN PADA BARIS SA TANPA PEMISAH (;)

"""
print("Python is fun!") print("Really!")

"""