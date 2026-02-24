#P Y T H O N   V A R I A B L E S
#1. || PYTHON VARIABLES ||
    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPILAN RAPIH

print("-------------------------------------------------------------------------------------------------")

    #A. CREATING VARIABLES
        #CONTOH 1

x = 18
y = "Jonathan"
print(x)
print(y)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2
        #VARIABEL TIDAK PERLU DIDEKLARASI DENGAN TIPE TERTENTU, 
        #BAHKAN DAPAT MENGUBAH TIPENYA SETELAH DITETAPKAN

x = 18           #x bertipe integer
x = "Jonathan"   #x sekarang bertipe string
print(x)

    #B. CASTING
        #CONTOH 1

x = str(5)    #x akan menjadi '5'
y = int(5)    #y akan menjadi 5
z = float(5)  #z akan menjadi 5,0

print("-------------------------------------------------------------------------------------------------")

    #C. GET THE TYPE
        #CONTOH 1

x = 18
y = "Jonathan"
print(type(x))
print(type(y))

print("-------------------------------------------------------------------------------------------------")

#2. || VARIABLE NAMES ||
    #DI BAGIAN KE DUA INI TIDAK AKAN MENAMPILKAN OUTPUT, KARENA INI TIDAK ADA PEMANGGIL NYA
    #SAYA HANYA INGIN MENCOBA PENGALAMAN MENGETIK NYA SAJA, AGAR LEBIH MUDAH MEMAHAMINYA

    #A. VARIABLE NAMES
        #CONTOH 1

myvar   = "Jonathan"
my_var  = "Jonathan"
_my_var = "Jonathan"
myVar   = "Jonathan"
MYVAR   = "Jonathan"
myvar2  = "Jonathan"

        #CONTOH SALAH

"""
2myvar  = "Jonathan"
my-var  = "Jonathan"
my var  = "Jonathan"

"""

    #B. CAMEL CASE
        #CONTOH 1

myVariableName = "Jonathan"

    #C. PASCAL CASE
        #CONTOH 1

MyVariableName = "Jonathan"

    #D. SNAKE CASE
        #CONTOH 1

my_variable_name = "Jonathan"

#3. || ASSIGN MULTIPLE VALUES ||
    #A. MANY VALUES TO MULTIPLE VARIABLES
        #CONTOH 1

x, y, z = "BAKSO", "NASI GORENG", "SEBLAK"
print(x)
print(y)
print(z)

print("-------------------------------------------------------------------------------------------------")

    #B. ONE VALUE TO MULTIPLE VARIABLES
        #CONTOH 1

x = y = z = "Semangka"
print(x)
print(y)
print(z)

print("-------------------------------------------------------------------------------------------------")

    #C. UNPACK A COLLECTION
        #CONTOH 1

ice_cream = ["coklat", "vanila", "strowberi"]
x, y, z = ice_cream
print(x)
print(y)
print(z)

print("-------------------------------------------------------------------------------------------------")

#4. || OUTPUT VARIABLES ||
    #A. OUTPUT VARIABLES
        #CONTOH 1

x = "Saya sedang belajar bahasa Python"
print(x)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

x = "Saya"
y = "mahasiswa"
z = "Universitas Riau"
print(x, y, z)

print("-------------------------------------------------------------------------------------------------")

        #ATAU BISA JUNGA MENGGUNAKAN OPERATOR "+"
        #CONTOH 3

x = "Saya"
y = "mahasiswa"
z = "Universitas Riau"
print(x + y + z)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 4

x = 10
y = 25
print(x + y)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH SALAH

"""
x = 18
y = "Jonathan"
print(x + y)

"""

        #SOLUSI NYA DENGAN MEMISAHKANNYA MENGGUNAKAN KOMA

x = 18
y = "Jonathan"
print(x, y)

print("-------------------------------------------------------------------------------------------------")

#5. || GLOBAL VARIABLES ||
    #A. GLOBAL VARIABLES
        #CONTOH 1

makanan = "bakso"

def pesan():
    print("Saya suka makan " + makanan)

pesan()

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

warna = "Biru"

def pesan():
    warna = "Hijau"
    print("Saya suka warna " + warna)

pesan()

print("Dia suka warna " + warna)

print("-------------------------------------------------------------------------------------------------")

    #B. THE GLOBAL KEYWORD
        #CONTOH 1

def pesan():
    global buah
    buah = "Apel"

pesan()

print("Saya sedang membeli buah " + buah)

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

game = "Mobile Legend"

def pesan():
    global game
    game = "Minecraft"

pesan()

print("Temanku suka bermain game " + game)

print("-------------------------------------------------------------------------------------------------")