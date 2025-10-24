def max_v1(a,b):
  return a if a>b else b
def max_v2(a,b):
  return max(a,b)
def max_v3(a,b):
  res = lambda a,b: a if a>b else b
  return res(a,b)

n = int(input('Enter first number '))
m = int(input('Enter second number '))
print(max_v1(n,m))
print(max_v2(n,m))
print(max_v3(n,m))