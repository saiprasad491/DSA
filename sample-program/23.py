
def sum_v1(n):
  s = 0
  while n!=0:
    d = n%10
    if d==2 or d==3 or d==5 or d==7:
      s += d
    n //= 10
  return s

def sum_v2(n):
  return sum([int(i) for i in str(n) if int(i) in [2,3,5,7]])

n = int(input('Enter a number '))
print(f"n = {n}, sum of prime digits of {n} is {sum_v1(n)}")
print(f"n = {n}, sum of prime digits of {n} is {sum_v2(n)}")





