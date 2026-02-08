#P Y T H O N   S T R I N G S
#1. || PYTHON STRINGS ||
    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPILAN RAPIH

print("-------------------------------------------------------------------------------------------------")

    #A. QUOTES INSIDE QUOTES

        #CONTOH 1

print("Ini adalah temanku")
print("Aku memanggilnya 'Farel'")
print('Aku memanggilnya "Farel"')

print("-------------------------------------------------------------------------------------------------")

    #B. ASSIGN STRING TO A VARIABLE

        #CONTOH 1

a = "Hii, apa kabar?"
print(a)

print("-------------------------------------------------------------------------------------------------")

    #C. MULTILINE STRINGS

        #CONTOH 1

a = """Ini adalah cara untuk 
    menampilan komentar
    di output"""
print(a)

print("-------------------------------------------------------------------------------------------------")

    #D. STRING ARE ARRAYS

        #CONTOH 1

a = "Hi, I'm Jonathan"
print(a[1])

#penjelasan : digunakan untuk pemanggilan indeks ke berapa

print("-------------------------------------------------------------------------------------------------")

    #E. LOOPING THROUGH A STRING

        #CONTOH 1

for x in "FaceBook":
  print(x)

#penjelasan : untuk membuat tampilan "FaceBook" menjadi ke bawah

print("-------------------------------------------------------------------------------------------------")

    #F. STRING LENGHT

        #CONTOH 1

a = "Saya suka bahasa pemrograman Python"
print(len(a))

#penjelasan : untuk mengecek ada berapa jumlah karakter didalam variabel a

print("-------------------------------------------------------------------------------------------------")

    #G. CHECK STRING

        #CONTOH 1

txt = "Bahasa pemrograman kesukaan saya adalah Python!"
print("Python" in txt)

#penjelasan : untuk mengecek apakah kata "Python" ada di dalam string txt 

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

txt = "Makanan kesukaan ku adalah bakso!"
if "bakso" in txt:
  print("betul, bakso adalah makanan kesukaan nya")

#penjelasan : untuk mengecek apakah kata "bakso" ada di dalam string txt

print("-------------------------------------------------------------------------------------------------")

    #H. CHECK IF NOT

        #CONTOH 1

txt = "Dia menyukai baju berwarna biru!"
print("hijau" not in txt)

#penjelasan : untuk mengecek apakah kata "hijau" tidak terdapat dalam string txt

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

txt = "Dia menyukai baju berwarna biru!"
if "hijau" not in txt:
  print("salah, jawaban mu tidak tepat")

#penjelasan : untuk mengecek apakah kata "hijau" tidak ada di dalam string txt

print("-------------------------------------------------------------------------------------------------")

#2. || SLICING STRINGS ||

    #A. SLICING

        #CONTOH 1

b = "Hii, aku Jonathan!"
print(b[1:5])

#penjelasan : untuk mengambil karakter dari indeks 1 sampai sebelum indeks 5

print("-------------------------------------------------------------------------------------------------")

    #B. SLICE FROM THE START

        #CONTOH 1

c = "Ini adalah kucingku!"
print(c[:10])

#penjelasan : untuk mengambil string dari awal (indeks 0) sampai indeks 10

print("-------------------------------------------------------------------------------------------------")

    #C. SLICE TO THE START

        #CONTOH 1

d = "Aku suka makan kue"
print(d[4:])

#penjelasan : untuk mengambil string mulai dari indeks ke-3 sampai akhir

print("-------------------------------------------------------------------------------------------------")

    #D. NEGATIVE INDEXING

        #CONTOH 1

e = "Aku senang bermain game"
print(e[-12:-5])

#penjelasan : untuk mengambil karakter dari indeks -12 sampai sebelum -5

print("-------------------------------------------------------------------------------------------------")

#3. || MODIFY STRINGS ||

    #A. UPPER CASE

        #CONTOH 1

a = "jonathan mulia surbakti"
print(a.upper())

#penjelasan : untuk membuat huruf kecil menjadi huruf besar semua

print("-------------------------------------------------------------------------------------------------")

    #B. LOWER CASE

        #CONTOH 1

b = "jONATHAn MuliA sURBAKTi"
print(b.lower())

#penjelasan : untuk membuat huruf besar menjadi kecil semua 

print("-------------------------------------------------------------------------------------------------")

    #C. REMOVE WHITESPACE

        #CONTOH 1

c = " Helo, apa kabar mu? "
print(c.strip()) 

#penjelasan : untuk membuat " Helo, apa kabar mu? " menjadi "Helo, apa kabar mu?"

print("-------------------------------------------------------------------------------------------------")

    #D. REPLACE STRING

        #CONTOH 1

d = "Sonathan Mulia Surbakti"     
print(d.replace("S", "J"))        

#penjelasan : untuk mengganti huruf S menjadi J, sehingga menghasilkan Jonathan Mulia Surbakti

print("-------------------------------------------------------------------------------------------------")

    #E. SPLIT STRING

        #CONTOH 1

e = "Saya suka,makan nasi goreng" 
print(e.split(","))               

#penjelasan : untuk memisahkan satu sring menjadi dua string ketika ada tanda koma

print("-------------------------------------------------------------------------------------------------")

#4. || CONCATENATION STRING ||

    #A. STRING CONCATENATION

        #CONTOH 1

a = "Jonathan"
b = "Mulia"
c = "Surbakti"
d = a + b + c
print(d)

print("-------------------------------------------------------------------------------------------------")

#penjelasan : digunakan untuk menggabungkan isi beberapa variabel agar 
              #memiliki output yang menjadi satu

        #CONTOH 2

a = "Jonathan"
b = "Mulia"
c = "Surbakti"
d = a + " " + b + " " + c
print(d)

print("-------------------------------------------------------------------------------------------------")

#penjelasan : digunakan untuk menggabungkan isi beberapa variabel agar 
              #memiliki output yang menjadi satu namu memiliki jarak spasi

#5. || FORMAT STRING ||

    #A. STRING FORMAT

        #CONTOH 1
        #CARA YANG SALAH

"""
age = 18
txt = "Nama ku Jonathan, Aku berumur " + age
print(txt)

"""

#penjelasan : Python tidak bisa langsung menggabungkan string dengan angka, 
              #seharusnya diganti menjadi

    #B. F-STRINGS

        #CONTOH 2

age = 18
txt = f"Nama ku Jonathan, Aku berumur {age}"
print(txt)

print("-------------------------------------------------------------------------------------------------")

        #ATAU

age = 18
txt = "Nama ku Jonathan, Aku berumur " + str(age)
print(txt)

print("-------------------------------------------------------------------------------------------------")

#KEDUA ITU ADALAH CARA YANG BENAR UNTUK MENGGABUNGKAN STRING DENGAN INTEGER

    #C. PLACEHOLDERS AND MODIFIERS

    #CONTOH 1

jumlah = 8
pesan = f"Jumlah barang ini ada {jumlah} banyak nya"
print(pesan)

#penjelasan : akan akan otomatis diisikan dengan nilai variabel jumlah, jadi angka 8 
              #dimasukkan ke dalam teks

print("-------------------------------------------------------------------------------------------------")

    #CONTOH 2

nilai = 98
pesan = f"Nilai rata rata ku {nilai:.2f} tingginya"
print(pesan)

#penjelasan : sama seperti sebelumnya, namun yang membedakan nilai yang bertipekan
              #integer/bilangan bulat berubah menjadi nilai yang bertipekan 
              #float/bilangan berkoma

print("-------------------------------------------------------------------------------------------------")

    #CONTOH 3

perhitungan = f"persegi panjang memiliki {10 * 20} luasnya"
print(txt)

print("-------------------------------------------------------------------------------------------------")

#penjelasan : disini nilai tidak perlu di deklarasi terlebih dahulu, 
              #namu langsung dijumlahkan dan langsung mengeluarkan hasil nya
                
#6. || ESCAPE CHARACTERS ||

    #A. ESCAPE CHARACTERS

        #CONTOH YANG SALAH

"""
txt = "Halo saya seorang "Mahasiswa" Universitas Riau."

"""
#penjelasan : gunakan karakter escape "\" untuk menyisipkan karakter yang tidak sah 
              #dalam sebuah string.

        #CONTOH YANG BENAR

txt = "Halo saya seorang \"Mahasiswa\" Universitas Riau."

print("-------------------------------------------------------------------------------------------------")

    #KARAKTER ESCAPE LAIN YANG DIGUNAKAN DI PYTHON:
    
        #KARAKTER 1 (SINGLE QUOTE)

pesan = 'It\'s oke, no problem.'
print(pesan) 

#penjelasan : digunakan pada kalimat yang memiliki petik satu atau dua

print("-------------------------------------------------------------------------------------------------")

        #KARAKTER 2 (BACKSLASH)

pesan = "Saya suka buah jeruk \\ semangka."
print(pesan)

#penjelasan : digunakan untuk memanggil garis miring beberapa pada kalimat

print("-------------------------------------------------------------------------------------------------")

        #KARAKTER 3 (NEW LINE)

pesan = "Jonathan\nMulia\nSurbakti"
print(pesan)

#penjelasan : digunakan untuk memisahkan lalu membuat baris baru pada kalimat

print("-------------------------------------------------------------------------------------------------")

        #KARAKTER 4 (CARRIAGE RETURN)

pesan = "Halo\rJonathan"
print(pesan) 

#penjelasan : hanya menampilkan kata atau kalimat setelah "\r"

print("-------------------------------------------------------------------------------------------------")

        #KARAKTER 5 (TAB)

pesan = "Dia\tdisana!"
print(pesan) 

#penjelasan : digunakan untuk membuat jarak spasi agak jauh pada kalimat atau yang disebut
              #tab

print("-------------------------------------------------------------------------------------------------")

        #KARAKTER 6 (BACKSPACE)

pesan = "Jonathan \bSurbakti!"
print(pesan) 

#penjelasan : digunakan untuk menghapus jarak spasi pada kalimat atau tidak memiliki spasi

print("-------------------------------------------------------------------------------------------------")

        #KARAKTER 7 (OCTAL VALUE)

txt = "\152\157\156\141\164\150\141\156"
print(txt) 

#penjelasan : garis miring terbalik diikuti oleh tiga angka akan menghasilkan nilai oktal

print("-------------------------------------------------------------------------------------------------")

        #KARAKTER 8 (HEX VALUE)

pesan = "\x6a\x6f\x6e\x61\x74\x68\x61\x6e"
print(pesan) 

#penjelasan : Garis miring terbalik diikuti dengan 'x' dan angka heksadesimal mewakili 
              #nilai heksadesimal

print("-------------------------------------------------------------------------------------------------")













   




