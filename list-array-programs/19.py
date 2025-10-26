
def fun(l1,l2):
  return l1+l2
def fun1(l1,l2):
  for i in l2:
    l1.append(i)
  return l1

l1 = [1,2,3]
l2 = [4,5,6]
print(fun(l1,l2))
print(fun1(l1,l2))