def fibonacci_series(n):
  a,b = 0,1
  if n==1 :
    print(0)
    return
  elif n==2:
    print(0,1)
    return
  else:
    print(0,1,end=" ")
    for i in range(n-2):
      c = a+b
      print(c,end=" ")
      a = b
      b = c

n = int(input('Enter a number '))
fibonacci_series(n)