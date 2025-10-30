def fun(s,ts):
  for i in range(len(s)):
    s = s[1:]+s[0]
    if ts==s:
      return True
  return False

print(fun("abcd","cdab"))
print(fun("abcd","cdabe"))