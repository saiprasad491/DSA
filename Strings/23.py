
def fun(s):
  l=[]
  for word in s.split(" "):
    if len(word) % 2 == 0:
      l.append(word.upper())
    else:
      l.append(word.lower())
  return " ".join(l)


s = input("Enter a string : ")
print(fun(s))



