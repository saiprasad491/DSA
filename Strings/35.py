
def fun(s):
  if len(s)<10:
    return False
  if not any(c.isupper() for c in s):
    return False
  if not any(c.islower() for c in s):
    return False
  if not any(c in "@#$-*" for c in s):
    return False
  return True
  

print(fun("hkNLCN2#sjkls"))