#P Y T H O N   M A T C H
#1. || PYTHON MATCH ||

    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPILAN RAPIH

print("-------------------------------------------------------------------------------------------------")

    #A. THE PYTHON MATCH STATEMENT

        #CONTOH 1

planet = 3
match planet:
  case 1:
    print("Merkurius")
  case 2:
    print("Venus")
  case 3:
    print("Bumi")
  case 4:
    print("Mars")
  case 5:
    print("Yupiter")
  case 6:
    print("Saturnus")
  case 7:
    print("Uranus")
  case 8:
    print("Neptunus")

#penjelasan : variabel planet memiliki nilai 3
              #jika memilih nilai 1, maka akan menampilkan "Merkurius"
              #jika memilih nilai 2, maka akan menampilkan "Venus"
              #jika memilih nilai 3, maka akan menampilkan "Bumi"
              #jika memilih nilai 4, maka akan menampilkan "Mars"
              #jika memilih nilai 5, maka akan menampilkan "Yupiter"
              #jika memilih nilai 6, maka akan menampilkan "Saturnus"
              #jika memilih nilai 7, maka akan menampilkan "Uranus"
              #jika memilih nilai 8, maka akan menampilkan "Neptunus"

print("-------------------------------------------------------------------------------------------------")

    #B. DEFAULT VALUE

        #CONTOH 1

kode_barang = 2
match kode_barang:
  case 3:
    print("Mie Instan")
  case 4:
    print("Minyak Makan")
  case 5:
    print("Gula Pasir")
  case _:
    print("Tidak ada kode barang dalam stok")

#penjelasan : variabel kode_barang memiliki nilai 2
              #jika variabel kode barang memiliki nilai 3
              #maka akan menampilkan "Mie Instan"
              #jika variabel kode barang memiliki nilai 4
              #maka akan menampilkan "Minyak Makan"
              #jika variabel kode barang memiliki nilai 5
              #maka akan menampilkan "Gula Pasir"
              #jika variabel kode barang memiliki nilai selain yang di atas
              #maka akan menampilkan "Tidak ada kode barang dalam stok"

print("-------------------------------------------------------------------------------------------------")

    #C. COMBINE VALUES

        #CONTOH 1

nilai = 90
match nilai:
  case 90 | 100:
    print("A+")
  case 70 | 80:
    print("B")
  case 50 | 60:
    print("C")
  case 30 | 40:
    print("D")
  case 10 | 20:
    print("E")

#penjelasan : nilai dari variabel nilai adalah 90
              #jika nilai dari variabel nilai adalah 90 dan 100
              #maka tampilkan "A+"
              #jika nilai dari variabel nilai adalah 70 dan 80
              #maka tampilkan "B"
              #jika nilai dari variabel nilai adalah 50 dan 60
              #maka tampilkan "C"
              #jika nilai dari variabel nilai adalah 30 dan 40
              #maka tampilkan "D" 
              #jika nilai dari variabel nilai adalah 10 dan 20
              #maka tampilkan "E"    

print("-------------------------------------------------------------------------------------------------")

    #C. IF STATEMENTS AS GUARDS

        #CONTOH 1

bulan = 2
hari = 3
match hari:
  case 1 | 2 | 3 | 4 | 5 if bulan == 1:
    print("Hari kerja di bulan Januari")
  case 1 | 2 | 3 | 4 | 5 if bulan == 2:
    print("Hari kerja di bulan Februari")
  case _:
    print("Tidak ditemukan")

#penjelasan = variabel bulan memiliki nilai 2
              #variabel hari memiliki nilai 3
              #jika variabel bulan memiliki nilai 1
              #jika variabel hari memiliki nilai 1,2,3,4,5
              #maka akan menampilkan "Hari kerja di bulan Januari"
              #jika variabel bulan memiliki nilai 2
              #jika variabel hari memiliki nilai 1,2,3,4,5
              #maka akan menampilkan "Hari kerja di bulan Februari"

print("-------------------------------------------------------------------------------------------------")


