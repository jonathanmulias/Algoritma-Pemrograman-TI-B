from myOOP import (
    ProdukElektronik,
    ProdukMakanan,
    Email,
    SMS,
    Mahasiswa
)

print("-------------------------------------------------------------------------------------------------")
print("SOAL 1")

tv = ProdukElektronik("TV", 3000000, "2 tahun")
roti = ProdukMakanan("Roti", 15000, "12-12-2026")

print(tv.nama_produk, "seharga", tv.harga, "dengan garansi", tv.garansi)
print(roti.nama_produk, "seharga", roti.harga, "kadaluarsa", roti.tanggal_kadaluarsa)

print("-------------------------------------------------------------------------------------------------")
print("SOAL 2")

email = Email("", "")
sms = SMS("", "")

for x in (email, sms):
  x.kirim()

print("-------------------------------------------------------------------------------------------------")
print("SOAL 3")

mhs = Mahasiswa(0)
mhs.set_nilai(85)
print(mhs.get_nilai())
print(mhs.get_status())