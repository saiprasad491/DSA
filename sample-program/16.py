
def rev_v1(n):
  rev = 0
  while(n>0):
    rev *= 10
    rev += n%10
    n//=10
  return rev
def rev_v2(n):
  s = str(n)
  return s[::-1]

n = int(input('Enter any number '))
print(f"Original number = {n} Reverse number = {rev_v1(n)}")
print(f"Original number = {n} Reverse number = {rev_v2(n)}")