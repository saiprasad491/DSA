def max_v1(a,b,c,d,e):
  return a if a>b and a>c and a>d and a>e else b if b>c and b>d and b>e else c if c>d and c>e else d if d>e else e
def max_v2(a,b,c,d,e):
  return max(a,b,c,d,e)
def max_v3(a,b,c,d,e):
  res = lambda a,b,c,d,e: a if (a>b and a>c and a>d and a>e) else b if b>c and b>d and b>e else c if c>d and c>e else d if d>e else e
  return res(a,b,c,d,e)
def max_v4(a,b,c,d,e):
  if a>b and a>c and a>d and a>e:
    return a
  elif b>c and b>d and b>e:
    return b
  elif c>d and c>e:
    return c
  elif d>e:
    return d
  else:
    return e
n = int(input('Enter first number '))
m = int(input('Enter second number '))
o = int(input('Enter third number '))
p = int(input('Enter fourth number '))
q = int(input('Enter fifth number '))
print(max_v1(n,m,o,p,q))
print(max_v2(n,m,o,p,q))
print(max_v3(n,m,o,p,q))
print(max_v4(n,m,o,p,q))