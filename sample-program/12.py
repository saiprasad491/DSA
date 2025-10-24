
def sum_v1(n):
  s = 0
  for i in range(1,n+1):
    s += i
  return s
def sum_v2(n):
  return n*(n+1)//2
def sum_v3(n):
  if n==1 or n==0:
    return n
  return n + sum_v3(n-1)

n = int(input('Enter n = '))
print(sum_v1(n))
print(sum_v2(n))
print(sum_v3(n))