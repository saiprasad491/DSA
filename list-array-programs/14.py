
def fun(l):
  l1 = []
  for i in l:
    if i not in l1:
      l1.append(i)
  return l1
l = [111,222,333,111,555,111]
print(fun(l))