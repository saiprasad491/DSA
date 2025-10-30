def fun(s):
  l = []
  for i in s.split(" "):
    l.append(i[0].upper()+i[1:].lower())
  return " ".join(l)

s = input("Enter a string : ")
print(fun(s))