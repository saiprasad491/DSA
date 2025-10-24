import math
def prime_v1(n):
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def prime_v2(n,i):
  if i==1:
    return True
  elif n%i==0:
    return False
  else:
    return prime_v2(n,i-1)


n = int(input('Enter a number '))
print(f"{n} is prime : {prime_v1(n)}")
print(f"{n} is prime : {prime_v2(n,n//2)}")

# for i in range(1,100):
#   if(prime_v1(i)):
#     print(f"{i} is prime : {prime_v1(i)}")
#   else:
#     print(i)


