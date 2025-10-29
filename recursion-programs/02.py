def fun(n):
  if n<=0:
    return
  print(n)
  return fun(n-1)
fun(5)