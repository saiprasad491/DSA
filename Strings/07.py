import re

def fun(s):
  return len(re.findall("[a-zA-Z]",s))

s = input("Enter a string value : ")
print(fun(s))


