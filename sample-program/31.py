import math
def strong(n):
  s = 0
  t = n
  while n!=0:
    d = n % 10
    s = s + math.factorial(d)
    n //= 10
  return s==t

for i in range(1,1001):
  if(strong(i)):
    print(f"{i} is strong number : {strong(i)}")