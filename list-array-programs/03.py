
def fun(L):
  l1,l2=[],[]
  for i in L:
    if i%2==0:
      l1.append(i)
    else:
      l2.append(i)
  return l1,l2
def fun1(L):
  l1,l2 = [x for x in L if x%2==0],[x for x in L if x%2!=0]
  return l1,l2

L = [1,2,3,4,5,6,7,8,9,10]
print(f"List={L} and even and odd separated = {fun(L)}")
print(f"List={L} and even and odd separated = {fun1(L)}")