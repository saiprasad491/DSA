def fun(s):
  res=""
  for i in range(len(s)):
    if i % 2 == 0:
      res += s[i].upper()
    else:
      res += s[i].lower()
  return res

s = input("Enter a string value : ")
print(fun(s))


