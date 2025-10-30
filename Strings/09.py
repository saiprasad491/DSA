import re

def fun(s):
  return len(re.findall("[ ]",s))

s = input("Enter a string : ")
print(fun(s))