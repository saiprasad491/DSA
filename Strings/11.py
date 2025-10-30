import re

def fun(s):
  return s[::-1]

def fun1(s):
  res=""
  for i in s:
    res = i+res
  return res


s = input("Enter a string : ")
print(fun(s))
print(fun1(s))