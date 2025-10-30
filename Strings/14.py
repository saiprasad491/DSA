def fun(s):
  res=""
  for i in s:
    if ord(i)>=65 and ord(i) <= 90:
      res += chr(ord(i)+32)
    else:
      res += chr(ord(i)-32)
  return res

def fun1(s):
  return s.swapcase()

s = input("Enter a string : ")
print(fun(s))
print(fun1(s))