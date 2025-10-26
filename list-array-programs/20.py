
def fun(l1,l2):
  return sorted(l1+l2)
def fun1(l1,l2):
  l3 = l1+l2
  l3.sort()
  return l3


l1 = [1,5,6,2,3,4]
l2 = [6,9,7,8,]
print(fun(l1,l2))
print(fun1(l1,l2))