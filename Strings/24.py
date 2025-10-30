def fun(s):
  n = len(s)
  if n % 2 != 0:
    return s[n//2]
  return s[n//2-1:n//2+1]

s = input("Enter a string : ")
print(fun(s))