
def fun(l):
  l.sort(reverse=True)
  return l[1]
def fun1(l):
  m = max(l)
  smax = None
  for i in l:
    if i != m:
      if smax==None:
        smax = i
      else:
        smax = max(smax,i)
  return smax

l=[11,2,34,67,15,111]
# print(fun(l))
print(fun1(l))