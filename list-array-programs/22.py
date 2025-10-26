
def fun(l1,l2):
  return list(set(l1+l2))
def fun1(l1,l2):
  for i in l2:
    if i not in l1:
      l1.append(i)
  return l1

l1 = [1,2,3,4]
l2 = [3,4,56,6]
print(fun(l1,l2))
print(fun1(l1,l2))