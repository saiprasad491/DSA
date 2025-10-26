

def fun(l1,l2):
  l3 = []
  for i in l2:
    if i in l1:
      l3.append(i)
  return l3

l1 = [1,2,3,4]
l2 = [3,4,56,6]
print(fun(l1,l2))