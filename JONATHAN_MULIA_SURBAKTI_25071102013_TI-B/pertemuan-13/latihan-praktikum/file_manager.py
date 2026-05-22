print("============================")
print("  PYTHON FILE MANAGER v1.0  ")
print("============================")

while True:
    print("\n[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[4] Exit")

    print("------------------------------")

    menu = int(input("Pilih menu : "))
    if menu == 4:
        break
    
    print("\nFile tersedia:")
    print("[1] catatan.txt")
    print("[2] tugas.txt")
    print("[3] jadwal.txt")

    file = int(input("Pilih file : "))
    
    if menu == 1 and file == 1:
        with open("catatan.txt", "r") as f:
            print(f.read())
    elif menu == 2 and file == 1:
        with open("catatan.txt", "w") as f:
            pesan = input("Masukkan Pesan : ")
            f.write(pesan)
    elif menu == 3 and file == 1:
        import os
        os.remove("catatan.txt")
    elif menu == 4:
        break

    if menu == 1 and file == 2:
        with open("tugas.txt", "r") as f:
            print(f.read())
    elif menu == 2 and file == 2:
        with open("tugas.txt", "w") as f:
            pesan = input("Masukkan Pesan : ")
            f.write(pesan)
    elif menu == 3 and file == 2:
        import os
        os.remove("tugas.txt")
    elif menu == 4:
        break

    if menu == 1 and file == 3:
        with open("jadwal.txt", "r") as f:
            print(f.read())
    elif menu == 2 and file == 3:
        with open("jadwal.txt", "w") as f:
            pesan = input("Masukkan Pesan : ")
            f.write(pesan)
    elif menu == 3 and file == 3:
        import os
        os.remove("jadwal.txt")
    elif menu == 4:
        break

