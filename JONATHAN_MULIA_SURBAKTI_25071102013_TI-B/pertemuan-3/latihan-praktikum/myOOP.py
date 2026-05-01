#A. INHERITANCE (Pewarisan)

class Produk:
  def __init__(self, nama_produk, harga):
    self.nama_produk = nama_produk
    self.harga = harga

  def info_produk(self):
    return self.nama_produk, self.harga

class ProdukElektronik(Produk):
  def __init__(self, nama_produk, harga, garansi):
    super().__init__(nama_produk, harga)
    self.nama_produk = nama_produk
    self.harga = harga
    self.garansi = garansi
    
  def info_produk(self):
    return self.nama_produk, self.harga, self.garansi

class ProdukMakanan(Produk):
  def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
    super().__init__(nama_produk, harga)
    self.nama_produk = nama_produk
    self.harga = harga
    self.tanggal_kadaluarsa = tanggal_kadaluarsa

  def info_produk(self):
    return self.nama_produk, self.harga, self.tanggal_kadaluarsa

#B. POLYMORPHISM

class Notifikasi:
  def __init__(self, notifikasi_email, notifikasi_sms):
    self.notifikasi_email = notifikasi_email
    self.notifikasi_sms = notifikasi_sms

class Email(Notifikasi):
  def kirim(self):
    print("Mengirim notifikasi melalui Email")

class SMS(Notifikasi):
  def kirim(self):
    print("Mengirim notifikasi melalui SMS")

#C. ESCAPSULATION

class Mahasiswa:
  def __init__(self, __nilai):
    self.__nilai = 0

  def set_nilai(self, _nilai):
    if 0 <= _nilai <= 100:
      self.__nilai = _nilai
    else:
      return "Tidak valid."
      exit()

  def get_nilai(self):
    return self.__nilai

  def get_status(self):
    if self.__nilai >= 60:
      return "Lulus"
    else:
      return "Gagal"
