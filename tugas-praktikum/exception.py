try:
    nilai1 = int(input("Masukkan angka pertama: "))
    nilai2 = int(input("Masukkan angka kedua: "))
    nilai3 = int(input("Masukkan angka ketiga: "))
    
    hasil = nilai1 + (nilai2 * nilai3)
    
    print("Hasil Perhitungan adalah:", hasil)

except ValueError:
    print("Error: Input harus berupa angka!")

except ZeroDivisionError:
    print("Error: Tidak bisa memasukkan nilai 0!")

else:
    print("Perhitungan berhasil dilakukan.")