def fun(s,p):
  for i in s:
    if i not in p:
      return False
  return len(s)==len(p)

print(fun("silent","listen"))
print(fun("abc","abd"))
print(fun("abcd","cabd"))