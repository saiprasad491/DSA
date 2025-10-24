

def count_digits_v1(n):
  c = 0
  while n>0:
    n%10
    c+=1
    n //= 10
  print(f"count = {c}")
def count_digits_v2(n):
  s = str(n)
  print(f"count = {len(s)}")
def count_digits_v3(n):
  if(n==0):
    return 0
  else:
    return 1+count_digits_v3(n//10)

n = int(input('Enter a number '))
count_digits_v1(n)
count_digits_v2(n)
print(f"count = {count_digits_v3(n)}")

