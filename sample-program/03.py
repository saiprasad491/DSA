def min_v1(a,b):
  return a if a<b else b
def min_v2(a,b):
  return min(a,b)
def min_v3(a,b):
  res = lambda a,b: a if a<b else b
  return res(a,b)

n = int(input('Enter 1st number '))
m = int(input('Enter 2nd number '))
print(min_v1(n,m))
print(min_v2(n,m))
print(min_v3(n,m))