#P Y T H O N   F O R   L O O P S
#1. || PYTHON FOR LOOPS ||
    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPILAN RAPIH

print("-------------------------------------------------------------------------------------------------")

    #A. PYTHON FOR LOOPS

        #CONTOH 1

warna = ["merah", "kuning", "hijau"]
for x in warna:
  print(x)

#penjelasan : variabel nama berisikan list string yaitu, merah, kuning, hijau
              #perulangan for untuk mengambil setiap item di dalam list warna, 
              #satu per satu, dan menyimpannya ke variabel x
              #tampilkan variabel x

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

for x in "Jonathan":
  print(x)

#penjelasan : perulangan for mengambil isi variabel x yaitu "Jonathan"
              #tampilkan variabel x yang sudah memiliki isi yaitu "Jonathan"

print("-------------------------------------------------------------------------------------------------")

    #B. THE BREAK STATEMENT

        #CONTOH 1

makanan = ["batagor", "siomay", "dimsum"]
for x in makanan:
  print(x)
  if x == "siomay":
    break
        
#penjelasan : variabel makanan berisikan list string yaitu, batagor, siomay, dimsum
              #perulangan for untuk mengambil setiap item di dalam list makanan, 
              #satu per satu, dan menyimpannya ke variabel x
              #tampilkan variabel x yang sudah diambil item nya tadi
              #jika variabel x adalah siomay, maka hentikan program

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

makanan = ["batagor", "siomay", "dimsum"]
for x in makanan:
  if x == "siomay":
    break
  print(x)

#penjelasan : sama seperti sebelumnya hanya saja yang membedakan, jika variabel x mengambil
              #list siomay, maka program nya berhenti dan tidak menampilkan siomay

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3

makanan = ["batagor", "siomay", "dimsum"]
for x in makanan:
  if x == "siomay":
    continue
  print(x)

#penjelasan : variabel makanan berisikan list string yaitu, batagor, siomay, dimsum
              #perulangan for untuk mengambil setiap item di dalam list makanan, 
              #satu per satu, dan menyimpannya ke variabel x
              #jika variabel x adalah siomay, maka hentikan program
              #jika tidak, tampilkan variabel x yang sudah diambil item nya tadi
              
print("-------------------------------------------------------------------------------------------------")

    #C. THE RANGE() FUNCTION

        #CONTOH 1

for x in range(5):
  print(x) 

#keterangan : program untuk menampilkan nilai variabel x sampai batas nilai nya 5

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

for x in range(5, 10):
  print(x) 

#keterangan : program untuk menampilkan nilai variabel x dari nilai 5 sampai 10

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3

for x in range(1, 30, 2):
  print(x)

#keterangan : program untuk menampilkan nilai variabel x dari nilai 1 sampai di bawah 30
              #namun dengan rentang atau jarak nya 2

print("-------------------------------------------------------------------------------------------------")

    #D. ELSE IN FOR LOOP

        #CONTOH 1 

for x in range(10):
  print(x)
else:
  print("Selesai!")    

#keterangan : program untuk menampilkan nilai variabel x dari nilai 1 sampai 10
              #jika nilai variabel x sudah sampai 10, maka tampilkan "Selesai!"       

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

for x in range(10):
  if x == 5: break
  print(x)
else:
  print("Selesai!")

#keterangan : program untuk menampilkan nilai variabel x dari nilai 1 sampai 10
              #jika nilai variabel x sudah sampai 5, maka hentikan program 

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3

makanan = ["Hamburger", "Pizza", "Hot dog"]
rasa = ["enak", "lezat", "sangat bagus"]

for x in makanan:
  for y in rasa:
    print(x, y)

#keterangan : program untuk menampilkan variabel x dan variabel y, dari masing masing list
              #berurutan
        
print("-------------------------------------------------------------------------------------------------")