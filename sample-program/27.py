def armstrong(n):
  s = 0
  t = n
  while n!=0:
    d = n % 10
    s = s + d ** 3
    n //= 10
  return s==t

for i in range(1,1001):
  if(armstrong(i)):
    print(f"{i} is armstrong : {armstrong(i)}")