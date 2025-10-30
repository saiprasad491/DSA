import re
def fun(s):   # ABiejk,rhjlasmlDWnjlk
  L = re.findall("[aeiouAEIOU]",s)
  print(L)  #['A', 'i', 'e', 'a']
  return len(L)

s = input("Enter string value : ")
v = 'aeiouAEIOU'
c=0
for i in s:
  if i in v:
    c+=1
    print(f"count = {c} char = {i}")

print("count = ",fun(s))
