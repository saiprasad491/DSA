
def fun(s):
  return s.lower()

def fun1(s):
  res = ""
  for i in s:
    res += i.lower()
  return res

def fun2(s):
  res = ""
  for i in s:
    res += chr(ord(i)+32)
  return res

s = input("Enter a string : ")
print(fun(s))
print(fun1(s))
print(fun2(s))