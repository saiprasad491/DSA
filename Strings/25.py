def fun(s):
  l = [i for i in s]
  return "".join(sorted(l))

s = input("Enter a string ")
print(fun(s))