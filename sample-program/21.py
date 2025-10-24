
def sum_v1(n):
  s = 0
  while n!=0:
    d = n%10
    if d%2==0:
      s += d
    n //= 10
  return s

def sum_v2(n):
  return sum([int(i) for i in str(n) if int(i)%2==0])

n = int(input('Enter a number '))
print(f"n = {n}, sum of even digits of {n} is {sum_v1(n)}")
print(f"n = {n}, sum of even digits of {n} is {sum_v2(n)}")





