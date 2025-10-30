import re

def fun(s):
  return re.sub("[^a-zA-Z0-9 ]","",s) 


s = "19jde@*20wikj#()"
print(fun(s))