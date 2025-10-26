
def fun(l):
  lstidx = len(l)-1
  ele = l[lstidx]
  i = lstidx-1
  while i > -1:
    l[i+1]=l[i]
    i-=1
  l[0] = ele
  return l
def fun1(l):
  n = len(l)-1
  return [l.pop(len(l)-1)]+l[0:n]
def fun2(l):
  n = len(l)-1
  return l[n:n+1]+l[0:n]
l = [1,2,3,4,5]
print(fun(l))
# print(fun1(l))
# print(fun2(l))