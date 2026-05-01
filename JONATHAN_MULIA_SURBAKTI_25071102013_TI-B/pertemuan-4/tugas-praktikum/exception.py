try:
    nilai1 = float(input("Masukkan angka pertama: "))
    nilai2 = float(input("Masukkan angka kedua: "))
    
    hasil = nilai1 / nilai2
    
    print("Hasil Pembagian adalah:", hasil)

except ValueError:
    print("Error: Input harus berupa angka!")

except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nilai 0!")

else:
    print("Pembagian berhasil dilakukan.")

