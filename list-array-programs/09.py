def fun(l):
  l.reverse()
  return l
def fun1(l,s,e):
  if not s<e:
    return l
  l[s],l[e] = l[e],l[s]
  return fun1(l,s+1,e-1)
l=[1,2,3,4,5]
# print(fun(l))
print(fun1(l,0,len(l)-1))