def isPrime(n,i):
  if i==1:
    return True
  if n%i==0:
    return False
  return isPrime(n,i-1)
for i in range(2,101):
  if isPrime(i,i//2):
    print(i,end=" ")