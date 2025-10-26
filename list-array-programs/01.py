
def fun(L):
  s = 0
  for i in L:
    s += i
  return s
def fun1(L):
  return sum(L)

L = [1,2,3,4,5]
print(f"List={L} and sum = {fun(L)}")
print(f"List={L} and sum = {fun1(L)}")