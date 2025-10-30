def fun(s):
  l=""
  for i in range(-1,-(len(s)+1),-1):
    l+=s[i]
  return l==s

s = input("Enter a string ")
print(f"{s} is palindrome {fun(s)}")