def fun(L):
  L[0] += L[len(L)-1]
  L[len(L)-1] = L[0] - L[len(L)-1]
  L[0] = L[0] - L[len(L)-1]
  return L
def fun1(L):
  L[0],L[-1] = L[-1],L[0]
  return L
L = [10,20,30]
# print(fun(L))
print(fun1(L))