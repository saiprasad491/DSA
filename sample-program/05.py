def min_v1(a,b,c):
  return a if a<b and a<c else b if b<c else c
def min_v2(a,b,c):
  return min(a,b,c)
def min_v3(a,b,c):
  res = lambda a,b: a if a<b and a<c else b if b<c else c
  return res(a,b)
def min_v4(a,b,c):
  if a<b and a<c:
    return a
  elif b<c:
    return b
  else:
    return c
  
n = int(input('Enter first number '))
m = int(input('Enter second number '))
o = int(input('Enter third number '))
print(min_v1(n,m,o))
print(min_v2(n,m,o))
print(min_v3(n,m,o))
print(min_v4(n,m,o))