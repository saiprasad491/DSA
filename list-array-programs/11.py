def fun(l):
  return max(l)
def fun1(l):
  m = l[0]
  for i in range(1,len(l)):
    if l[i] > m:
      m = l[i]
  return m

l = [11,9,2,94,23]
print(fun(l))
print(fun1(l))