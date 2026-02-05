#P Y T H O N   F U N C T I O N 
#1. || PYTHON ARGUMENTS ||
    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPILAN RAPIH

print("-------------------------------------------------------------------------------------------------")

    #A. ARGUMENTS

        #CONTOH 1

def my_function(nama):
  print(nama + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#keterangan : program ini memanggil satu persatu variabel nama dari my_function, lalu
              #menampilkan kembali dengan tambahan kalimat " Refsnes"

print("-------------------------------------------------------------------------------------------------")

    #B. NUMBER ARGUMENTS

        #CONTOH 1

def my_function(nama_awal, nama_akhir):
  print(nama_awal + " " + nama_akhir)

my_function("Jonathan", "Surbakti")

print("-------------------------------------------------------------------------------------------------")

    #C. DEFAULT PARAMETER VALUES

        #CONTOH 1

def my_function(nama = "Jonathan"):
  print("Hello", nama)

my_function("Rizki")
my_function("Farel")
my_function()
my_function("Dimas")

#keterangan : pada program ini, isi dari variabel nama bisa di letakkan di barisan awal atau
              #bisa dibuat terpisah

print("-------------------------------------------------------------------------------------------------")

    #D. KEYWORD ARGUMENTS

        #CONTOH 1

def my_function(hewan, nama):
  print("Aku memiliki seekor", hewan)
  print("peliharaan ku", hewan + " nama nya", nama)

my_function(hewan = "kucing", nama = "Kitty")

#keterangan : pada program ini hanya memanggil isi dari variabel yang sudah ada lalu 
              #memanggilnya kembali

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2 (JIKA DIGANTI SUBJEK NYA)

def my_function(hewan, nama):
  print("I have a", hewan)
  print("My", hewan + "'s name is", nama)

my_function(nama = "Kitty", hewan = "Kucing")

print("-------------------------------------------------------------------------------------------------")

        #BISA JUGA MENGGUNAKAN CARA SEPERTI INI

def my_function(hewan, nama):
  print("I have a", hewan)
  print("My", hewan + "'s name is", nama)

my_function("Kucing", "Kitty")

print("-------------------------------------------------------------------------------------------------")

        #SAMA SEPERTI CARA SEBELUMNYA NAMUN INI DIGANTI SUBJEK NYA

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Kitty", "Kucing")

print("-------------------------------------------------------------------------------------------------")

        #MENAMBAHKAN VARIABEL UMUR BERTIPE DATAKAN INTEGER

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

print("-------------------------------------------------------------------------------------------------")

    #E. PASSING DIFFERENT DATA TYPES

        #CONTOH 1

def my_function(buah):
  for buah in buah:
    print(buah)

buah_ku = ["Nanas", "Semangka", "Sirsak"]
my_function(buah_ku)

#keterangan : memanggil list satu persatu pada variabel buah_ku

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

def my_function(person):
  print("Nama:", person["Nama"])
  print("Umur:", person["Umur"])

my_person = {"Nama": "Jonathan", "Umur": 18}
my_function(my_person)

#keterangan : memanggil list satu persatu lalu menampilkan nya bersama "Nama :" dan "Umur :"

print("-------------------------------------------------------------------------------------------------")

    #F. RETURN VALUES

        #CONTOH 1

def my_function(x, y):
  return x + y

result = my_function(4, 5)
print(result)

#keterangan : program untuk melakukan perhitungan penjumlahan du nilai

print("-------------------------------------------------------------------------------------------------")

    #G. RETURNING DIFFERENT DATA TYPES

        #CONTOH 1

def my_function():
  return ["biru", "ungu", "orange"]

warna = my_function()
print(warna[0])
print(warna[1])
print(warna[2])

#keterangan : program untuk memanggil list pada variabel warna sesuai dengan indeks keberapa

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

def my_function():
  return (54, 32)

nilai1, nilai2 = my_function()
print("nilai 1:", nilai1)
print("nilai 2:", nilai2)

#keterangan : program untuk memanggil variabel sesuai dengan nilai yang telah dibuat, lalu
              #menampilkan nya sesuai dengan variabel yang sudah dipanggil
              #print("nilai 1:", nilai1)
              #print("nilai 2:", nilai2)

print("-------------------------------------------------------------------------------------------------")

    #H. POSITIONAL-ONLY ARGUMENTS

        #CONTOH 1

def my_function(nama, /):
  print("Halo", nama)

my_function("Jonathan")

#catatan : menentukan bahwa suatu fungsi hanya dapat memiliki argumen posisional.
           #untuk menentukan argumen hanya berdasarkan posisi, tambahkan , /setelah 
           #argumen:

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2 (TANPA "/")

def my_function(nama):
  print("Halo", nama)

my_function(nama = "Jonathan")

print("-------------------------------------------------------------------------------------------------")

    #I. KEYWORD-ONLY ARGUMENTS

        #CONTOH 1

#catatan : untuk menentukan bahwa suatu fungsi hanya dapat memiliki argumen kata kunci, 
           #tambahkan *, sebelum argumen

def my_function(*, nama):
  print("Helo", nama)

my_function(nama = "Jonathan")

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

#catatan : tanpa "*" juga boleh 

def my_function(nama):
  print("Halo", nama)

my_function("Jonathan")

print("-------------------------------------------------------------------------------------------------")

    #J. KEYWORD-ONLY ARGUMENTS

        #CONTOH 1

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(10, 13, c = 16, d = 21)
print(result)

#catatan : dapat menggabungkan kedua tipe argumen dalam fungsi yang sama. Argumen sebelum 
           #/hanya berupa argumen posisional, dan argumen setelah *hanya berupa argumen kata kunci

print("-------------------------------------------------------------------------------------------------")
