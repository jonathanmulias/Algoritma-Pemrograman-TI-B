#P Y T H O N   I F . . .   E L S E
#1. || PYTHON IF || 
    #print("----------") DIGUNAKAN AGAR OUTPUT NYA MEMILIKI PEMISAH GARIS DAN MEMILIKI TAMPILAN RAPIH

print("-------------------------------------------------------------------------------------------------")

    #A. PYTHON IF STATEMENT

        #CONTOH 1 (PERNYATAAN IF)

a = 50
b = 100
if b > a:
  print("b lebih besar dari a")

#penjelasan : jika nilai b lebih besar dari nilai a, maka tampilkan "b lebih besar dari a"

print("-------------------------------------------------------------------------------------------------")

    #B. IF STATEMENTS WORK

        #CONTOH 1 (MEMERIKSA APAKAH SUATU ANGKA POSITIF)

nilai = 15
if nilai > 0:
  print("angka ini positif")

#penjelasan : jika nilai pada variabel nilai > 0, maka tampilkan "angka ini positif"

print("-------------------------------------------------------------------------------------------------")

    #C. MULTIPLE STATEMENTS IN IF BLOCK

        #CONTOH 1 (BEBERAPA PERNYATAAN DALAM BLOK IF)

umur = 20
if umur >= 17:
  print("Kamu sudah dewasa")
  print("lebih serius lagi dalam menjalani hidup")
  print("Carilah pengalaman yang berguna untuk kedepan nya")

#penjelasan : nilai umur adalah 20, jika lebih besar dari 17, maka tampilkan 
              #"Kamu sudah dewasa"
              #"lebih serius lagi dalam menjalani hidup"
              #"Carilah pengalaman yang berguna untuk kedepan nya"

print("-------------------------------------------------------------------------------------------------")

    #D. USING VARIABLES IN CONDITIONS

        #CONTOH 1 (MENGGUNAKAN VARIABEL BOOLEAN)

masuk = True
if masuk:
  print("Selamat Datang!")

#penjelasan : nilai dari variabel masuk adalah True, karena nilai variabel masuk True,
              #maka tampilkan selamat datang

print("-------------------------------------------------------------------------------------------------")

#2. || PYTHON ELIF || 

    #A. PYTHON ELIF STATEMENT

        #CONTOH 1

a = 20
b = 20
if b > a:
  print("b lebih besar daripada a")
elif a == b:
  print("a dan b bernilai sama")

#penjelasan : nilai dari variabel a dan b adalah 20, jika nilai b lebih besar dari a maka
              #tampilkan "b lebih besar daripada a", jika tidak maka tampilkan 
              #"a dan b bernilai sama"

print("-------------------------------------------------------------------------------------------------")

    #B. MULTIPLE ELIF STATEMENTS

        #CONTOH 1

umur = 13

if umur >= 50:
  print("Kamu sudah tua")
elif umur >= 17:
  print("Kamu sudah dewasa")
elif umur >= 12:
  print("Kamu sudah remaja")
elif umur >= 4:
  print("Kamu sudah anak anak")
elif umur <= 4:
  print("Kamu belum anak anak")

#penjelasan : nilai dari variabel umur adalah 13
              #jika niali variabel umur lebih besar dari 50, maka tampilkan
              #"Kamu sudah tua"
              #jika niali variabel umur lebih besar dari 17, maka tampilkan
              #"Kamu sudah dewasa"
              #jika niali variabel umur lebih besar dari 12, maka tampilkan
              #"Kamu sudah remaja"
              #jika niali variabel umur lebih besar dari 6, maka tampilkan
              #"Kamu sudah anak anak"

print("-------------------------------------------------------------------------------------------------")

          #CONTOH 2

bulan = 3

if bulan == 1:
  print("Januari")
elif bulan == 2:
  print("Februari")
elif bulan == 3:
  print("Maret")
elif bulan == 4:
  print("April")
elif bulan == 5:
  print("Mei")
elif bulan == 6:
  print("Juni")
elif bulan == 7:
  print("Juli")
elif bulan == 8:
  print("Agustus")
elif bulan == 9:
  print("september")
elif bulan == 10:
  print("oktober")
elif bulan == 11:
  print("November")
elif bulan == 12:
  print("Desember")
elif bulan >= 12:
  print("Tidak terdefinisi")

#penjelasan : nilai variabel bulan adalah 3
              #jika nilai variabel bulan adalah 1, maka tampilkan "Januari"
              #jika nilai variabel bulan adalah 2, maka tampilkan "Februari"
              #jika nilai variabel bulan adalah 3, maka tampilkan "Maret"
              #jika nilai variabel bulan adalah 4, maka tampilkan "April"
              #jika nilai variabel bulan adalah 5, maka tampilkan "Mei"
              #jika nilai variabel bulan adalah 6, maka tampilkan "Juni"
              #jika nilai variabel bulan adalah 7, maka tampilkan "Juli"
              #jika nilai variabel bulan adalah 8, maka tampilkan "Agustus"
              #jika nilai variabel bulan adalah 9, maka tampilkan "september"
              #jika nilai variabel bulan adalah 10, maka tampilkan "oktober"
              #jika nilai variabel bulan adalah 11, maka tampilkan "November"
              #jika nilai variabel bulan adalah 12, maka tampilkan "Desember"
              #jika nilai variabel bulan lebih besar dari 12, maka tampilkan "Tidak terdefinisi"

print("-------------------------------------------------------------------------------------------------")

#3. || PYTHON ELSE || 

    #A. PYTHON ELSE STATEMENT

        #CONTOH 1

a = 101
b = 100
if b > a:
  print("b lebih besar daripada a")
elif a == b:
  print("a dan b bernilai sama")
else:
  print("a lebih besar dari b")

#penjelasan : nilai dari variabel a adalah 101 dan nilai dari variabel b adalah 100,
              #jika nilai b lebih besar dari a maka tampilkan "b lebih besar daripada a",
              #jika tidak maka tampilkan a dan b bernilai sama"
              #jika tidak keduanya maka tampilkan "a lebih besar dari b"

print("-------------------------------------------------------------------------------------------------")

    #B. ELSE WITHOUT ELIF

        #CONTOH 1

a = 50
b = 25
if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

#penjelasan : nilai dari variabel a adalah 50 dan nilai dari variabel b adalah 25,
              #jika nilai b lebih besar dari a, maka tampilkan "b lebih besar dari a"
              #jika tidak maka tampilkan "b tidak lebih besar dari a"

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

nomor = 8

if nomor % 2 == 0:
  print("Bilangan ini genap")
else:
  print("Bilangan ini ganjil")

#penjelasan : nilai dari variabel nomor adalah 8, 
              #jika nilai dari variabel bisa dibagi 2, maka tampilkan "Bilangan ini genap"
              #jika nilai dari variabel bisa tidak bisa dibagi 2, maka tampilkan 
              #"Bilangan ini ganjil"

print("-------------------------------------------------------------------------------------------------")

    #C. COMPLETE IF-ELIF-ELSE CHAIN

        #CONTOH 1

waktu_menit_perebusan = 10

if waktu_menit_perebusan > 11:
  print("sangat matang")
elif waktu_menit_perebusan > 9:
  print("matang")
elif waktu_menit_perebusan > 6:
  print("setengah matang")
else:
  print("mentah")

#penjelasan : nilai dari variabel waktu_menit_perebusan adalah 10,
              #jika nilai variabel nya lebih besar dari 11, maka tampilkan "sangat matang"
              #jika nilai variabel nya lebih besar dari 9, maka tampilkan "matang"
              #jika nilai variabel nya lebih besar dari 6, maka tampilkan "setengah matang"
              #jika nilai variabel nya tidak semua yang disebutkan diatas, maka tampilkan
              #"mentah"

print("-------------------------------------------------------------------------------------------------")

    #D. ELSE AS FALLBACK

        #CONTOH 1

nama = "Jonathan"

if len(nama) > 0:
  print(f"Halo, selamat datang {nama}!")
else:
  print("Error: nama tidak ditemukan")

#penjelasan : Pernyataan `else` berfungsi untuk cadangan yang akan dieksekusi 
              #ketika tidak ada satu pun kondisi sebelumnya yang benar

print("-------------------------------------------------------------------------------------------------")

#4. || SHORTHAND IF || 

    #A. SHORT HAND IF

        #CONTOH 1

a = 10
b = 5
if a > b: print("a lebih besar dari b")
              
#penjelasan : nilai variabel a adalah 10, nilai variabel b adalah 5,
              #jika nilai a lebih besar dari b, maka tampilkan "a lebih besar dari b"

print("-------------------------------------------------------------------------------------------------")

    #B. SHORT HAND IF ... ELSE

      #CONTOH 1

a = 5
b = 550
print("A") if a > b else print("B")

#penjelasan : nilai variabel a adalah 5, nilai variabel b adalah 550,
              #tampilkan "A" jika nilai a lebih besar dari b
              #jika tidak maka tampilka "B"

print("-------------------------------------------------------------------------------------------------")

    #C. ASSIGN A VALUE WITH IF ... ELSE

        #CONTOH 1

a = 20
b = 50
nilai_besar = a if a > b else b
print("nilai yang paling besar adalah", nilai_besar)

#penjelasan : nilai variabel a adalah 20, nilai variabel b adalah 50,
              #variabel nilai besar akan berisikan sebuah nilai jika
              #nilai a lebih besar dari b maka tampilkan nilai a
              #nilai a lebih kecil dari b maka tampilkan nilai b
              #tampilkan "nilai yang paling besar adalah", dengan nilai setelah di proses

print("-------------------------------------------------------------------------------------------------")

    #D. MULTIPLE CONDITIONS ON ON LINE

        #CONTOH 1

a = 550
b = 551

print("A") if a > b else print("=") if a == b else print("B")

#penjelasan : nilai variabel a adalah 550, nilai variabel b adalah 551,
              #tampilkan "A" jika nilai a lebih besar dari b
              #jika tidak, tampilka "=" jika nilai a dan b sama
              #jika tidak, tampilkan "B" jika 2 kondisi di atas tidak terpenuhi atau
              #nilai a lebih kecil dari b

print("-------------------------------------------------------------------------------------------------")

    #D. PRACTICAL EXAMPLES

        #CONTOH 1

nama = ""
tampil_nama = nama if nama else "Guest"
print("Welcome,", tampil_nama)

#penjelasan : isi dari variabel nama adalah tidak ada
              #variabel tampil_nama akan menampilkan nama jika variabel nama ada isi
              #jika tidak, variabel nama akan berisi "Guest"
              #tampilkan "Welcome,", sama variabel tampil_nama

print("-------------------------------------------------------------------------------------------------")
  
#5. || LOGICAL OPERATORS || 

    #A. PYTHON LOGICAL OPERATORS

        #CONTOH 1 (THE AND OPERATOR)

a = 300
b = 20
c = 660
if a > b and c > a:
  print("Kedua konsisi tersebut benar")

#penjelasan : nilai dari variabel a adalah 300
              #nilai dari variabel b adalah 20
              #nilai dari variabel c adalah 660
              #jika nili a lebih besar dari b dan nilai c lebih besar dari a maka,
              #tampilkan "Kedua konsisi tersebut benar"

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2 (THE OR OPERATOR)

a = 300
b = 20
c = 660
if a > b or c > a:
  print("Setidaknya salah satu kondisi tersebut benar")

#penjelasan : nilai dari variabel a adalah 300
              #nilai dari variabel b adalah 20
              #nilai dari variabel c adalah 660
              #jika nili a lebih besar dari b atau nilai c lebih besar dari a maka,
              #tampilkan "Setidaknya salah satu kondisi tersebut benar"

print("-------------------------------------------------------------------------------------------------")

          #CONTOH 1 (THE NOT OPERATOR)

a = 50
b = 789
if not a > b:
  print("a TIDAK lebih besar dari b")

#penjelasan : nilai dari variabel a adalah 50
              #nilai dari variabel b adalah 789
              #jika nilai a lebih besar dari b, namun menggunakan gerbang logika not,
              #hasil nya menjadi a tidak lebih besar dari b, maka tampilkan
              #"a TIDAK lebih besar dari b"

print("-------------------------------------------------------------------------------------------------")

    #B. COMBINING MULTIPLE OPERATORS

        #CONTOH 1

umur = 30
pelajar = False
kode_diskon = True

if (umur < 17 or umur > 50) and not pelajar or kode_diskon:
  print("Diskon Berlaku!")

#penjelasan : variabel umur harus bernilai di bawah 17 dan di atas 50
              #bukan pelajar dan punya kode diskon
              #syarat nya terpenuhi, karena bukan pelajar, dan memiliki kode_diskon

print("-------------------------------------------------------------------------------------------------")

    #C. USING PARENTHESES FOR CLARITY

        #CONTOH 1

suhu_tubuh = 40
flu = False
wajah_pucat = True

if (suhu_tubuh > 38 and not flu) or wajah_pucat:
  print("Kondisi sedang demam, periksakan ke dokter")

#penjelasan : nilai variabel suhu_tubuh adalah 40
              #nilai variabel flu adalah False
              #nilai variabel wajah_pucat adalah True
              #jika suhu tubuh diatas 38 dan tidak flu, tetapi wajah pucat
              #maka tampilkan "Kondisi sedang demam, periksakan ke dokter"

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

nama = "Jonathan"
password = "jonathan123"
verifikasi = False

if nama and password and verifikasi:
  print("Login berhasil")
else:
  print("Login gagal")

#penjelasan : isi dari variabel nama adalah "Jonathan"
              #isi dari variabel password adalah "jonathan123"
              #nilai dari variabel verifikasi adalah False
              #jika variabel nama sudah terisi
              #variabel password sudah terisi
              #dan variabel verifikasi memiliki nilai True
              #maka tampilkan "Login berhasil"
              #jika salah satu belum ter isi atau verifikasi nilai nya false maka,
              #tampilkan "Login gagal"

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3

nilai = 30
#nilai harus dari 1 - 100, tidak boleh kurang dan lebih
if nilai >= 0 and nilai <= 100:
  print("nilai ada")
else:
  print("nilai belum ada")

#penjelasan : variabel nilai berisikan nilai 30
              #jika nilai dari variabel nilai lebih besar dari 0 dan lebih kecil dari 100
              #maka tampilkan "nilai ada"
              #jika tidak, maka tampilkan "nilai belum ada"

print("-------------------------------------------------------------------------------------------------")

#5. || NASTED IF || 

    #A. NASTED IF STATEMENTS

        #CONTOH 1

x = 15

if x > 10:
  print("Di atas 10")
  if x > 20:
    print("Di atas 20 juga")
  else:
    print("Tetapi tidak di atas 20")

#penjelasan : nilai variabel x adalah 15
              #jika nilai x lebih besar dari 10
              #maka tampilkan "Di atas 10"
              #jika nilai x lebih besar dari 20
              #maka tampilkan "Di atas 20 juga"
              #jika nilai x tidak lebih besar dari 20
              #maka tampilkan "Tetapi tidak di atas 20"

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 2

umur = 18
sim = False

if umur >= 17:
  if sim:
    print("kamu boleh membawa kendaraan")
  else:
    print("harus punya sim terlebih dahulu")
else:
  print("dilarang membawa kendaraan di bawah umur 17 tahun")
  
#penjelasan : nilai dari variabel umur adalah 18
              #nilai dari variabel sim adalah False
              #jika umur lebih dari 17 dan memiliki sim maka,
              #tampilkan "kamu boleh membawa kendaraan"
              #jika tidak memiliki sim maka,
              #tampilkan ""harus punya sim terlebih dahulu"
              #jika umur lebih kecil dari 17 maka,
              #tampilkan "dilarang membawa kendaraan di bawah umur 17 tahun"

print("-------------------------------------------------------------------------------------------------")

        #CONTOH 3

nilai = 78
kehadiran = 92
tugas_proyek = False

if nilai >= 75:
  if kehadiran >= 90:
    if tugas_proyek:
      print("Sangat memuaskan")
    else:
      print("Bagus, tapi kurang di tugas proyek")
  else:
    print("Bagus, tapi kurang di kehadiran")
else:
  print("Maaf, anda gagal!")

#penjelasan : nilai dari variabel nilai adalah 78
              #nilai dari variabel kehadiran adalah 92
              #nilai dari variabel tugas_proyek adalah False
              #jika variabel nilai memiliki nilai lebih dari 75
              #jika variabel kehadiran memiliki nilai lebih dari 90
              #jika variabel tugas_proyek memiliki nilai True
              #maka tampilkan "Sangat memuaskan"
              #jika variabel nilai memiliki nilai lebih dari 75,
              #namun variabel tugas_proyek memiliki nilai False maka,
              #tampilkan "Bagus, tapi kurang di tugas proyek"
              #jika variabel nilai memiliki nilai lebih dari 75,
              #namun variabel kehadiran memiliki nilai di bawah 90 maka,
              #tampilkan "Bagus, tapi kurang di kehadiran"
              #jika semua kondisi tidak terpenuhi di seperti di atas maka,
              #tampilkan "Maaf, anda gagal!"

print("-------------------------------------------------------------------------------------------------")

    #B. NASTED IF VS LOGICAL OPERATORS

      #CONTOH 1

temparatur = 23
cuaca_cerah = True

if temparatur > 20:
  if cuaca_cerah:
    print("Bagusnya pergi ke pantai!")

#penjelasan : nilai dari variabel temparatur adalah 30
              #nilai dari variabel cuaca_cerah True
              #jika variabel temparatur memiliki nilai lebih besar dari 20
              #jika variabel cuaca_cerah memiliki nilai true
              #maka tampilkan "Bagusnya pergi ke pantai!"

print("-------------------------------------------------------------------------------------------------")

      #CONTOH 2 (MENGGUNAKAN AND)

temparatur = 23
cuaca_cerah = True

if temparatur > 20 and cuaca_cerah:
  print("Bagusnya pergi ke pantai!")

#penjelasan : nilai dari variabel temparatur adalah 30
              #nilai dari variabel cuaca_cerah True
              #jika variabel temparatur memiliki nilai lebih besar dari 20
              #dan variabel cuaca_cerah memiliki nilai true
              #maka tampilkan "Bagusnya pergi ke pantai!"

print("-------------------------------------------------------------------------------------------------")

      #CONTOH 3 

username = "Jonathan"
password = "jonathan123"
keaktifan_akun = True

if username:
  if password:
    if keaktifan_akun:
      print("Login berhasil")
    else:
      print("akun tidak aktif")
  else:
    print("Memerlukan Password")
else:
  print("Memerlukan Username")

#penjelasan : isi dari variabel username adalah "Jonathan"
              #isi dari variabel password adalah "jonathan123"
              #nilai dari variabel keaktifan_akun adalah True
              #jika isi dari variabel username ada
              #jika isi dari variabel password ada
              #jika nila dari variabel keaktifan_akun True
              #maka tampilkan "Login berhasil"
              #jika nila dari variabel keaktifan_akun False
              #maka tampilkan "akun tidak aktif"
              #jika isi dari variabel password tidak ada
              #maka tampilkan "Memerlukan Password"
              #jika isi dari variabel username tidak ada
              #maka tampilkan "Memerlukan Username"

print("-------------------------------------------------------------------------------------------------")

      #CONTOH 4

nilai = 95
keaktifan = 6

if nilai >= 90:
  if keaktifan > 2:
    print("A+")
  else:
    print("A-")
elif nilai >= 80:
  print("B+")
else:
  print("C")       

#penjelasan : nilai dari variabel nilai adalah 95
              #nilai dari variabel keaktifan adalah 6
              #jika variabel nilai memiliki nilai lebih besar dari 90
              #jika variabel keaktifan memiliki nilai lebih besar dari 2
              #maka tampilkan "A+"
              #jika variabel keaktifan memiliki nilai lebih kecil dari 2
              #maka tampilkan "A-"
              #jika variabel nilai memiliki nilai lebih besar dari 80
              #maka tampilkan "B+"
              #jika variabel nilai memiliki nilai lebih kecil dari 80
              #maka tampilkan "C"

print("-------------------------------------------------------------------------------------------------")


