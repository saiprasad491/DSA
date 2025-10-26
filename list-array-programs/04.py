
def fun(n):
  l1,l2=[x for x in range(n+1) if x%2==0],[x for x in range(n+1) if x%2!=0]
  return l1,l2


even,odd = fun(10)
print(even)
print(odd)



