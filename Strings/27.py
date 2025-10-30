def fun(s):
  l = []
  for i in s:
    if i not in l:
      l.append(i)
  return ''.join(l)


s = "abcabcdabdsj"
print(fun(s))