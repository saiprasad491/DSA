import math

def fun(n):
  c = 0
  f = math.factorial(n)
  while f!=0:
    if f%10 != 0:
      break
    c = c+1
    f //= 10
  return c

n = int(input('Enter a number '))
print(f"number = {n} fact = {math.factorial(n)} and training 0s = {fun(n)}")