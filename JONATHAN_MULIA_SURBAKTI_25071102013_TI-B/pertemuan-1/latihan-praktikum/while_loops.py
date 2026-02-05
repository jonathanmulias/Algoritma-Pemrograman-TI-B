#P Y T H O N   W H I L E   L O O P S
#1. || PYTHON WHILE LOOPS ||
    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPILAN RAPIH

print("-------------------------------------------------------------------------------------------------")

    #A. WHILE LOOPS
        #CONTOH 1

i = 1
while i < 5:
  print(i)
  i += 1

#penjelasan : variabel i memiliki nilai adalah 1
              #pelakukan perulangan jika i kurang dari 6, 1 < 6
              #tampilkan 1
              #1 + 1 = 2, sekarang nilai i adalah 2

              #pelakukan perulangan jika i kurang dari 6, 2 < 6
              #tampilkan 2
              #2 + 1 = 3, sekarang nilai i adalah 3

              #pelakukan perulangan jika i kurang dari 6, 3 < 6
              #tampilkan 3
              #3 + 1 = 4, sekarang nilai i adalah 4

              #pelakukan perulangan jika i kurang dari 6, 4 < 6
              #tampilkan 4
              #4 + 1 = 5, sekarang nilai i adalah 5

              #karena perulangan sudah sampai ke 5
              #maka tidak akan melakukan perulangan lagi

print("-------------------------------------------------------------------------------------------------")

    #B. THE BREAK SATAEMENT

        #CONTOH 1

i = 0
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#penjelasan : variabel i memiliki nilai adalah 0
              #pelakukan perulangan jika i kurang dari 6, 0 < 6
              #tampilkan 0
              #jika nilai i sama dengan 3, maka hentikan program
              #0 + 1 = 1, sekarang nilai i adalah 1

              #variabel i memiliki nilai adalah 1
              #pelakukan perulangan jika i kurang dari 6, 1 < 6
              #tampilkan 1
              #jika nilai i sama dengan 3, maka hentikan program
              #1 + 1 = 2, sekarang nilai i adalah 2

              #variabel i memiliki nilai adalah 2
              #pelakukan perulangan jika i kurang dari 6, 2 < 6
              #tampilkan 2
              #jika nilai i sama dengan 3, maka hentikan program
              #2 + 1 = 3, sekarang nilai i adalah 2

print("-------------------------------------------------------------------------------------------------")

    #C. THE CONTINUE STATEMENT

        #CONTOH 1

i = 0
while i < 5:
  i += 1
  if i == 3:
    continue
  print(i)

#penjelasan : sama seperti cara yang sebelumnya, namun yang membedakan disni adalah
              #jika ni i adalah 3, maka nilai nya tidak perlu ditampilkan

print("-------------------------------------------------------------------------------------------------")

    #D. THE ELSE STATEMENT

        #CONTOH 1

i = 0
while i < 5:
  print(i)
  i += 1
else:
  print("i tidak dibawah angka 5 lagi")

#penjelasan : nilai dari variabel i adalah 0
              #melakukan perulangan jika nilai i lebih kecil dari 5, 0 < 5
              #tampilkan 0
              #0 + 1 = 1
              
              #nilai dari variabel i adalah 1
              #melakukan perulangan jika nilai i lebih kecil dari 5, 1 < 5
              #tampilkan 1
              #1 + 1 = 2

              #nilai dari variabel i adalah 2
              #melakukan perulangan jika nilai i lebih kecil dari 5, 2 < 5
              #tampilkan 2
              #2 + 1 = 3

              #nilai dari variabel i adalah 3
              #melakukan perulangan jika nilai i lebih kecil dari 5, 3 < 5
              #tampilkan 3
              #3 + 1 = 4

              #nilai dari variabel i adalah 4
              #melakukan perulangan jika nilai i lebih kecil dari 5, 4 < 5
              #tampilkan 4
              #4 + 1 = 5

              #nilai dari variabel i adalah 5
              #melakukan perulangan jika nilai i lebih kecil dari 5, 5 < 5
              #sekarang nilai i tidak lebih kecil lagi dari 5
              #tampilkan 
              #"i tidak dibawah angka 5 lagi"

print("-------------------------------------------------------------------------------------------------")