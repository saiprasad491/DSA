
def fun(l):
  ele = l[0]
  i = 0
  while i < len(l)-1:
    l[i]=l[i+1]
    i+=1
  l[len(l)-1] = ele
  return l
def fun1(l):
  l.append(l.pop(0))
  return l
def fun2(l):
  return l[1:]+l[0:1]
l = [1,2,3,4,5]
# print(fun(l))
# print(fun1(l))
print(fun2(l))