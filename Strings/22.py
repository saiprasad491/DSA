def fun(s):
  l = []
  for i in s.split(" "):
    if len(i)==1:
      l.append(i.lower())
    else:
      l.append(i[0].lower()+i[1:len(i)-1].upper()+i[-1].lower())
  return " ".join(l)

s = input("Enter a string : ")
print(fun(s))