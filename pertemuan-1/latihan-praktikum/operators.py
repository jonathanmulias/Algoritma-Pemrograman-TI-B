#P Y T H O N   O P E R A T O R S
#1. || PYTHON OPERATORS ||
    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPILAN RAPIH

print("-------------------------------------------------------------------------------------------------")

    #A. PYTHON OPERATORS

        #CONTOH 1

print(10 + 5)

print("-------------------------------------------------------------------------------------------------")

#penjelasan : operator digunakan untuk melakukan perhitungan pada dua variabel atau lebih
              #pada contoh diatas menggunakan operator "+"

        #CONTOH 2

sum1 = 10 + 50      # 60 (10 + 50)
sum2 = sum1 + 70   # 130 (60 + 70)
sum3 = sum2 + sum2   # 260 (130 + 130)

print(sum1)
print(sum2)
print(sum3)

print("-------------------------------------------------------------------------------------------------")

#2. || ARITHMETIC OPERATORS ||
    #A. ARITHMETIC OPERATORS

        #CONTOH 1

x = 6
y = 4

print(x + y)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

x = 6
y = 4

print(x - y)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3

x = 6
y = 4

print(x * y)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 4

x = 16
y = 2

print(x / y)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 5

x = 6
y = 4

print(x % y)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 6

x = 6
y = 4

print(x ** y) #sama dengan 6*6*6*6

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 7

x = 16
y = 3

print(x // y) #membulatkan hasil ke bawah ke bilangan bulat terdekat

print("-------------------------------------------------------------------------------------------------")

#3. || ASSIGNMENT OPERATORS ||
    #A. ASSIGNMENT OPERATORS

        #CONTOH 1 (=)

x = 8
print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2 (+=)

x = 8
x += 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3 (-=)

x = 8
x -= 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 4 (*=)

x = 8
x *= 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 5 (/=)

x = 5
x /= 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 6 (%=)

x = 8
x%=2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 7 (//=)

x = 8
x//=2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 8 (**=)

x = 8
x **= 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 9 (&=)

x = 8
x &= 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 10 (|=)

x = 8
x |= 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 11 (^=)

x = 8
x ^= 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 12 (>>=)

x = 8
x >>= 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 13 (<<=)

x = 8
x <<= 2

print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 14 (:=)

print(x := 8)

print("-------------------------------------------------------------------------------------------------")

    #B. THE WALRUS OPERATOR

        #CONTOH 1

nilai = [1, 2, 3, 4, 5]

if (count := len(nilai)) > 2:
    print(f"List has {count} elements")

print("-------------------------------------------------------------------------------------------------")

#4. || COMPARISON OPERATORS ||
    #A. COMPARISON OPERATORS

x = 8
y = 2

print(x == y) #CONTOH 1
print(x != y) #CONTOH 2
print(x > y)  #CONTOH 3
print(x < y)  #CONTOH 4
print(x >= y) #CONTOH 5
print(x <= y) #CONTOH 6

print("-------------------------------------------------------------------------------------------------")

    #B. CHAINING COMPARISON OPERATORS

        #CONTOH 1

x = 8

print(1 < x < 15)

print(1 < x and x < 15)

print("-------------------------------------------------------------------------------------------------")

#5. || LOGICAL OPERATORS ||
    #A. LOGICAL OPERATORS

        #CONTOH 1

x = 99

print(x > 0 and x < 100)

#keterangan : untuk menguji apakah suatu angka lebih besar dari 0 dan kurang dari 100

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

x = 50

print(x < 50 or x > 100)

#keterangan : untuk menguji apakah suatu angka kurang dari 50 atau lebih besar dari 100

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3

x = 55

print(not(x > 10 and x < 100))

#keterangan : membalikkan hasil dengan not

print("-------------------------------------------------------------------------------------------------")

#6. || IDENTITY OPERATORS ||
    #A. IDENTITY OPERATORS

        #CONTOH 1

x = ["MERAH", "KUNING"]
y = ["MERAH", "KUNING"]
z = x

print(x is z)
print(x is y)
print(x == y)

#penjelasan : operator is akan mengembalikan nilai True jika kedua variabel menunjuk 
              #ke objek yang sama

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

x = ["HIJAU", "BIRU"]
y = ["HIJAU", "BIRU"]

print(x is not y)

#penjelasan : operator is notakan mengembalikan nilai True jika kedua variabel tidak 
              #menunjuk ke objek yang sama

print("-------------------------------------------------------------------------------------------------")

    #A. DIFFERENCE BETWEEN is and ==
        #CONTOH 1
        
x = [10, 20, 30]
y = [10, 20, 30]

print(x == y)
print(x is y)

#penjelasan : is - Memeriksa apakah kedua variabel menunjuk ke objek yang sama di memori.
              #== - Memeriksa apakah nilai kedua variabel sama

print("-------------------------------------------------------------------------------------------------")

#7. || MEMBERSHIP OPERATORS ||
    #A. MEMBERSHIP OPERATORS

        #CONTOH 1

makanan = ["ketoprak", "nasi goreng", "gado gado"]

print("batagor" in makanan)

#penjelasan : untuk memeriksa apakah "batagor" ada di dalam daftar

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

makanan = ["ketoprak", "nasi goreng", "gado gado"]

print("bakso" not in makanan)

#penjelasan : untuk memeriksa apakah "bakso" ada di dalam daftar

print("-------------------------------------------------------------------------------------------------")

    #A. MEMBERSHIP IN STRINGS
        #CONTOH 1

text = "Jonathan Mulia Surbakti"

print("u" in text)
print("joko" in text)
print("Y" not in text)

#catatan : operator keanggotaan juga bekerja dengan string

print("-------------------------------------------------------------------------------------------------")

#8. || BITWISE OPERATORS ||
    #A. BITWISE OPERATORS

        #CONTOH 1 (OPERATOR AND "&")

print(5 & 8)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2 (OPERATOR OR "|")

print(5 | 8)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3 (OPERATOR XOR "^")

print(5 ^ 8)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 4 (OPERATOR NOT "~")

print(~3)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 5 (OPERATOR ZERO FILL LEFT SHIFT "<<")

print(3 << 2)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 6 (OPERATOR SIGNED RIGHT SHIFT ">>")

print(8 >> 2)

print("-------------------------------------------------------------------------------------------------")

#9. || OPERATOR PRECEDENCE ||
    #A. OPERATOR PRECEDENCE

        #CONTOH 1

print((5 + 4) - (5 + 4))
"""
tanda kurung memiliki prioritas tertinggi, dan perlu dievaluasi terlebih dahulu.
perhitungan di atas berbunyi 9 - 9 = 0

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

print(100 + 5 * 3)
"""
perkalian * didahulukan dulu daripada penjumlahan +, oleh karena itu perkalian 
dievaluasi sebelum penjumlahan

"""

print("-------------------------------------------------------------------------------------------------")

    #B. PRECEDENCE ORDER

        #CONTOH 1

print(50 + ~2)
"""
operasi bitwise NOT memiliki prioritas lebih tinggi daripada penjumlahan, dan perlu dievaluasi terlebih dahulu.
perhitungan di atas berbunyi 50 + -2 = 96

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

print(100 - 5 * 3)
"""
perkalian * didahulukan dulu daripada pengurangan -, oleh karena itu perkalian 
dievaluasi sebelum pengurangan

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3

print(12 >> 5 - 3)
"""
pergeseran bit ke kanan memiliki prioritas lebih rendah daripada pengurangan, 
dan kita perlu menghitung pengurangan terlebih dahulu. perhitungan di atas 
berbunyi 12 >> 3 = 3

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 4

print(10 & 2 + 3)
"""
operasi bitwise AND memiliki prioritas lebih rendah daripada penjumlahan, 
dan kita perlu menghitung penjumlahan terlebih dahulu. Perhitungan di atas 
berbunyi 10 & 5 = 0

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 5

print(10 ^ 1 + 2)
"""
operasi XOR bitwise memiliki prioritas lebih rendah daripada penjumlahan, 
dan kita perlu menghitung penjumlahan terlebih dahulu. Perhitungan di atas 
adalah 10^3 = 9

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 6

print(10 | 2 + 3)
"""
operasi bitwise OR memiliki prioritas lebih rendah daripada penjumlahan, 
dan kita perlu menghitung penjumlahan terlebih dahulu. Perhitungan di atas 
berbunyi 10 | 5 = 15

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 7

print(3 == 2 + 1)
"""
perbandingan "seperti" memiliki prioritas lebih rendah daripada penjumlahan, 
dan kita perlu menghitung penjumlahan terlebih dahulu. perhitungan di atas 
berbunyi 3 == 3 = Benar

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 8

print(not 10 == 10)
"""
operator logika NOT memiliki prioritas lebih rendah daripada perbandingan "like", 
dan kita perlu menghitung perbandingannya terlebih dahulu. perhitungan di atas 
berbunyi: not True = False

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 9

print(5 or 7 and 10)
"""
operator "dan" memiliki prioritas lebih tinggi daripada operator "atau", 
dan kita perlu menghitung ekspresi "dan" terlebih dahulu. perhitungan di atas
berbunyi: 5 atau 10 = 5

"""

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 10

print(2 or 5 + 3 or 1)
"""
operator "atau" memiliki prioritas lebih rendah daripada penjumlahan, 
dan kita perlu menghitung penjumlahan terlebih dahulu. perhitungan di atas 
berbunyi: 2 atau 8 atau 1 = 2
"""

print("-------------------------------------------------------------------------------------------------")