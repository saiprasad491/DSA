def max_v1(a,b,c):
  return a if a>b and a>c else b if b>c else c
def max_v2(a,b,c):
  return max(a,b,c)
def max_v3(a,b,c):
  res = lambda a,b: a if a>b and a>c else b if b>c else c
  return res(a,b)

n = int(input('Enter first number '))
m = int(input('Enter second number '))
o = int(input('Enter third number '))
print(max_v1(n,m,o))
print(max_v2(n,m,o))
print(max_v3(n,m,o))