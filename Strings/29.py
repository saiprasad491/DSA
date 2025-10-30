import re

def fun(s):
  return re.sub("[aeiouAEIOU]","",s)

s = input("Enter a string : ")
print(fun(s))