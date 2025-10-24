def evenOdd_v1(n):
  return n%2==0
def evenOdd_v2(n):
  return (n&1)==0

n = int(input("Enter a number : "))
print(evenOdd_v1(n))
print(evenOdd_v2(n))