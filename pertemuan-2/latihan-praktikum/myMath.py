"""
==================================================
           PRAKTIKUM PYTHON - MODUL
==================================================

Buatlah sebuah modul Python bernama:

    myMath.py

Di dalam modul tersebut harus terdapat beberapa fungsi
matematika dasar berikut:

"""

#1. penambahan(a, b)
#- Mengembalikan hasil penjumlahan dua bilangan.

def penjumlahan(a,b):
    return a + b

#2. pengurangan(a, b)
#- Mengembalikan hasil pengurangan dua bilangan.

def pengurangan(a,b):
    return a - b

#3. perkalian(a, b)
#- Mengembalikan hasil perkalian dua bilangan.

def perkalian(a,b):
    return a * b

#4. pembagian(a, b)
#- Mengembalikan hasil pembagian dua bilangan.
#- Jika b = 0, tampilkan pesan error:
#"Pembagian tidak dapat dilakukan karena pembagi bernilai 0".

def pembagian1(a,b):
    if b == 0:
        return("embagian tidak dapat dilakukan karena pembagi bernilai 0")
    else:
        return a / b

#5. modulus(a, b)
#- Mengembalikan sisa hasil bagi dua bilangan.

def pembagian2(a,b):
    return a / b

#6. fibonacci(n)
#- Mengembalikan deret Fibonacci sebanyak n angka pertama.

def fibonaci(n):
  if n <= 1:
    return n
  else:
    return fibonaci(n - 1) + fibonaci(n - 2)
  



    



