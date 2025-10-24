def swap_v1(a,b):
  temp = a
  a = b
  b = a
  print("a = ",a,"b = ",b)
def swap_v2(a,b):
  a,b = b,a
  print("a = ",a,"b = ",b)
def swap_v3(a,b):
  a = a+b
  b = a-b
  a = a-b
  print("a = ",a,"b = ",b)
def swap_v4(a,b):
  a = a*b
  b = a//b
  a = a//b
  print("a = ",a,"b = ",b)
def swap_v5(a,b):
  a = a^b
  b = a^b
  a = a^b
  print("a = ",a,"b = ",b)
def swap_v6(a,b):
  a = a+b-(b:=a)
  print(f"a = {a} ,b = {b}")
             
a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
swap_v1(a,b)
swap_v2(a,b)
swap_v3(a,b)
swap_v4(a,b)
swap_v5(a,b)
swap_v6(a,b)