
def fun(l):  
  l1 = l
  return l1 == sorted(l)
def fun1(l):  
  for i in range(len(l)-1):
    print(i)
    if l[i]>l[i+1]: return False
  return True

l=[1,2,3,4,5]
print(f"{l} is sorted : {fun(l)}")
print(f"{l} is sorted : {fun1(l)}")