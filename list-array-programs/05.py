
def fun(l,m):
  l1=[x for x in l if x<m]
  return l1

l=[11,9,15,12,3,7,14,10]
smaller = fun(l,10)
print(smaller)



