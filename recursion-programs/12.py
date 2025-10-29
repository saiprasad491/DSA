def subsets(s,ans,idx):
  if idx==len(s):
    if len(ans) == 0:
      print("empty string")
    else:
      print(ans)
    return
  subsets(s,ans+s[idx],idx+1)
  subsets(s,ans,idx+1)
subsets("123","",0)
