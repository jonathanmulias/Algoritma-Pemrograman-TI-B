def myfunc():
  x = 300
  print(x)

myfunc()

print("-------------------------------------------------------------------------------------------------")

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print("-------------------------------------------------------------------------------------------------")

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

print("-------------------------------------------------------------------------------------------------")

x = range(3, 10)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))

print("-------------------------------------------------------------------------------------------------")

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)

