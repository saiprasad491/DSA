def fun(s):
  L = []
  index = 0
  for i in s.split():
    L.append(i[::-1])
  index += 1
  return " ".join(L)
s = input("Enter a string : ")
print(fun(s))