import math

def pow_v1(a,b):
  v = a
  if b==0: return 1
  for i in range(b-1):
    a *= v
  return a
def pow_v2(a,b):
  return pow(a,b)
def pow_v3(a,b):
  return a**b
def pow_v4(a,b):
  return math.pow(a,b)

x = int(input('Enter value of x = '))
y = int(input('Enter value of y = '))
print(f"{x} to the power {y} = {pow_v1(x,y)}")
print(f"{x} to the power {y} = {pow_v2(x,y)}")
print(f"{x} to the power {y} = {pow_v3(x,y)}")
print(f"{x} to the power {y} = {pow_v4(x,y)}")