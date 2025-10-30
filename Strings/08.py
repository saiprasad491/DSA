import re

def fun(s):
  return len(re.findall("[0-9]",s))

s = input("Enter any string value : ")
print(fun(s))