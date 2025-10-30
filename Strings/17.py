def fun(s):
  res = ""
  l = s.split(" ")
  for i in range(len(l)):
    if i%2==0:
      res += (l[i])[::-1] + " "
    else:
      res += l[i] + " "
  return res

s = input("Enter a string : ")
print(fun(s))

