
def sum_v1(n):
  s = 0
  while n!=0:
    d = n%10
    s += d
    n //= 10
  return s

def sum_v2(n):
  return sum([int(i) for i in str(n)])

n = int(input('Enter a number '))
print(f"n = {n}, sum of digits of {n} is {sum_v1(n)}")
print(f"n = {n}, sum of digits of {n} is {sum_v2(n)}")





