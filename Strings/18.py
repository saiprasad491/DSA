def fun(s):
  L = []
  index = 0
  for i in s.split():
    if index % 2 !=0:
      L.append(i[::-1])
    else:
      L.append(i)
    index += 1
  return " ".join(L)
s = input("Enter a string : ")
print(fun(s))