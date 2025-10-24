
def digits_extraction_v1(n):
  while n>0:
    print(n%10)
    n //= 10
  print("---------")
def digits_extraction_v2(n):
  s = str(n)
  for i in s[::-1]:
    print(i)
  print("---------")

n = int(input('Enter a number '))
digits_extraction_v1(n)
digits_extraction_v2(n)

