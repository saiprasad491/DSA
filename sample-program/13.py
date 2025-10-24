import math

def fact_v1(n):
  f=1
  for i in range(1,n+1):
    f*=i
  return f
def fact_v2(n):
  if n==0 or n==1:
    return 1
  return n * fact_v2(n-1)
def fact_v3(n):
  return math.factorial(n)

n=int(input('Enter a number '))
print(f"Factorial of {n} using v1 ",fact_v1(n))
print(f"Factorial of {n} using v2 ",fact_v2(n))
print(f"Factorial of {n} using v3 ",fact_v3(n))