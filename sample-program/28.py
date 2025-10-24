def perfect(n):
  s = 0
  for i in range(1,n):
    if n % i == 0:
      s += i
      if s>n:
        return False
  return s==n

n = int(input('Enter a number '))
print(f"{n} is perfect number : {perfect(n)}")