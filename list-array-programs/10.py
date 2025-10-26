def fun(l,x):
  if x not in l : return None
  return l.index(x)
def fun1(l,x):
  for i in range(len(l)):
    if l[i]==x:
      return i
  return None

l=[11,22,33,44,55]
x = -11
print(fun(l,x))
print(fun1(l,x))