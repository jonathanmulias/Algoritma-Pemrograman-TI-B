#P Y T H O N   B O O L E A N S
#1. || PYTHON BOOLEANS ||
    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPI

print("-------------------------------------------------------------------------------------------------")

    #A. BOOLEAN VALUES

        #CONTOH 1

print(5 > 6)
print(3 == 2)
print(4 < 6)

#penjelasan : membandingkan dua nilai, ekspresi tersebut dievaluasi dan Python 
              #mengembalikan jawaban boolean

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

a = 90
b = 220

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#penjelasan : Cetak pesan berdasarkan apakah kondisinya benar Trueatau salah False
              #jika 220 > 90 cetak "b is greater than a" jika tidak maka cetak
              #"b is not greater than a"

print("-------------------------------------------------------------------------------------------------")

    #B. EVALUATE VALUES AND VARIABLES

        #CONTOH 1

print(bool("Jonathan"))
print(bool(18))

#penjelasan : untuk mengevaluasi sebuah string dan sebuah angka

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

nama = "Jonathan"
umur = 18

print(bool(nama))
print(bool(umur))

#penjelasan : untuk mengevaluasi dua variabel

    #B. MOST VALUES ARE TRUE

        #CONTOH 1

bool("pqrs")
bool(789)
bool(["red", "green", "blue"])

#penjelasan : untuk mengembalikan nilai true

    #C. SOME VALUES ARE FALSE

        #CONTOH 1

bool(True)
bool(None)
bool(10)
bool("")
bool((""))
bool([""])
bool({""})

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

class kelas():
  def __len__(self):
    return 0

pekerjaan = kelas()
print(bool(pekerjaan))

#penjelasan : dievaluasi menjadi False, dan terjadi jika memiliki objek yang 
              #dibuat dari kelas dengan __len__fungsi yang mengembalikan 0atau False:

print("-------------------------------------------------------------------------------------------------")

    #D. FUNCTIONS CAN RETURN A BOOLEAN

        #CONTOH 1

def kesimpulan() :
  return False

print(kesimpulan())

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

def kesimpulan() :
  return True

if kesimpulan():
  print("IYAAAA!")
else:
  print("TIDAKK!")

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3

nilai = 300
print(isinstance(nilai, int))

print("-------------------------------------------------------------------------------------------------")