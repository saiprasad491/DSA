def max_v1(a,b,c,d):
  return a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
def max_v2(a,b,c,d):
  return max(a,b,c,d)
def max_v3(a,b,c,d):
  res = lambda a,b,c,d: a if (a>b and a>c and a>d) else b if b>c and b>d else c if c>d else d
  return res(a,b,c,d)
def max_v4(a,b,c,d):
  if a>b and a>c and a>d:
    return a
  elif b>c and b>d:
    return b
  elif c>d:
    return c
  else:
    return d
n = int(input('Enter first number '))
m = int(input('Enter second number '))
o = int(input('Enter third number '))
p = int(input('Enter fourth number '))
print(max_v1(n,m,o,p))
print(max_v2(n,m,o,p))
print(max_v3(n,m,o,p))
print(max_v4(n,m,o,p))