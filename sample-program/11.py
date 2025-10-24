
def abs_v1(n):
  return n * -1 if n<0 else n
def abs_v2(n):
  return abs(n)

n = int(input('Enter a number : '))
print(abs_v1(n))
print(abs_v2(n))

