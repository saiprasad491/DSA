def tribonacci_series(n):
  a,b,c = 0,1,2
  if n==1 :
    print(0)
    return
  elif n==2:
    print(0,1)
    return
  elif n==3:
    print(0,1,2)
    return
  else:
    print(0,1,2,end=" ")
    for i in range(n-2):
      d = a+b+c
      print(d,end=" ")
      a = b
      b = c
      c = d

n = int(input('Enter a number '))
tribonacci_series(n)