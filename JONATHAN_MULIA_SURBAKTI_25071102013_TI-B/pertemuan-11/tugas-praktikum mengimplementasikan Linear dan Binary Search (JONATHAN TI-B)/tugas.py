"""
Buatlah sebuah program yang mengimplementasikan Linear Search.
Dengan catatan data nya adalah : data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9].
Tampilkan data dan minta pengguna untuk memasukkan nilai berapa yang dicari, jika ketemu maka tampilkan index nya, jika tidak maka return -1.
Buatlah dalam 1 file saja
"""

data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]
print(data)
n = int(input("masukkan data nilai yang ingin dicari : "))

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

x = n

result = linearSearch(data, x)

if result != -1:
    print("data di temukan pada indeks ke : ", result)
else:
    print("data tidak ditemukan / -1")

"""
Buatlah sebuah program yang mengimplementasikan Binary Search.
Dengan catatan data nya adalah : data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9].
Tampilkan data dan minta pengguna untuk memasukkan nilai berapa yang dicari, jika ketemu maka tampilkan index nya, jika tidak maka return -1.
Buatlah dalam 1 file saja
"""

# Binary search memerlukan data yang sudah diurutkan

data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]
print("\ndata sebelum diurutkan", data)
data.sort()
print("data setelah diurutkan", data)
n = int(input("masukkan data nilai yang ingin dicari : "))

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

x = n

result = binarySearch(data, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")

