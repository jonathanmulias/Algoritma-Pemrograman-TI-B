jumlah = int(input("masukkan jumlah data yang inggin dimasukkan : "))
mylist = []

for i in range(jumlah):
    try:
        data = int(input("masukkan data " + str(i + 1) + " : "))
        if data < 0:
          print("data yang dimasukkan tidak boleh negatif")
        else:
          mylist.append(data)
    except:
      print("data harus bilangan bulat")

print("sebelum diubah", mylist)
def radix_sort(mylist):
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(mylist)
    exp = 1

    while maxVal // exp > 0:

        while len(mylist) > 0:
            val = mylist.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                mylist.append(val)

        exp *= 10

    return mylist

def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mysortedlist = mergeSort(mylist)
radixSort = radix_sort(mylist)
print("\nSorted array:", mysortedlist)
print("Radix sort:", radixSort)