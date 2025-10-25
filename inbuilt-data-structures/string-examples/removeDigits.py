def removeDigits(s):
  li=[]
  for i in s:
    if not i.isdigit():
      li.append(i)
  return "".join(li)

s = input("Enter any string ")
print(removeDigits(s))


