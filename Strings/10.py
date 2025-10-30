import re

def fun(s):
  return len(re.findall("[^0-9a-zA-Z ]",s))

s = input("Enter a string : ")
print(fun(s))