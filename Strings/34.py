def fun(s):
  for i in range(97,123):
    if chr(i) not in s.lower():
      print(i)
      return False
  return True
s = "The quick brown fox jumps over the lazy dog"
print(fun(s))