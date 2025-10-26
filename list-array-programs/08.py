def fun(L,x):
  L = [n for n in L if n>x]
  return len(L)

L = [1,2,3,4,5,6]
x = 2
print(fun(L,x))