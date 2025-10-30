def fun(s):
  l = []
  for i in s.split():
    if fun1(i):
      l.append(i)
  l.sort(key=fun2,reverse=True)
  return l[0]
def fun2(s):
  return len(s)
def fun1(s):
  l=""
  for i in range(-1,-(len(s)+1),-1):
    l+=s[i]
  return l==s

s = "a ab abc aca madam malayalam"
print(fun(s))