import re
def fun(s):   # prakash
  L = []
  if s.isalpha():
    L = re.findall("[^aeiouAEIOU]",s)
    print(L)  #['p', 'r', 'k', 's', 'h']
  return len(L)

s = input("Enter string value : ")
v = 'aeiouAEIOU'
c=0
for i in s:
  if i not in v:
    c+=1
    print(f"count = {c} char = {i}")

print("count = ",fun(s))
