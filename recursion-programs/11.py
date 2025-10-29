def permutations(s,ans):
  if len(s) == 0:
    print(ans)
    return 
  for i in range(0,len(s)):
    permutations(s[:i]+s[i+1:],ans+s[i])
permutations("abc","")






