film = [[ "Danur", 50000 ], [ "Inside Out 2", 45000 ], [ "Transfomers", 50000 ], [ "Tenki no ko", 45000], [ "Alice in Borderland", 50000]]

print(film)

film_yang_ditonton = int(input("Masukkan nomor film yang ingin anda tonton : "))

for data in film:
    if film_yang_ditonton == 1:
        film_yang_ditonton = film[0]
        print(f"1 {film[0]}")
        break
    elif film_yang_ditonton == 2:
        film_yang_ditonton = film[1]
        print(f"2 {film[1]}")
        break
    elif film_yang_ditonton == 3:
        film_yang_ditonton = film[2]
        print(f"3 {film[2]}")
        break
    elif film_yang_ditonton == 4:
        film_yang_ditonton = film[3]
        print(f"4 {film[3]}")
        break
    elif film_yang_ditonton == 5:
        film_yang_ditonton = film[4]
        print(f"5 {film[4]}")
        break
    else:
        print("Film tidak ditemukan")
