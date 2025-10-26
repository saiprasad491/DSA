from collections import deque
def fun(l,d):
  n = len(l)
  d = d%n
  return l[d:]+l[:d]
def fun1(l,d):
  dq = deque(l)
  dq.rotate(-i)
  return list(dq)
def fun2(l,d):
  for i in range(d):
    l.append(l.pop(0))
  return l
def reverse(l,s,e):
  while s<e:
    l[s],l[e] = l[e],l[s]
    s += 1
    e -= 1
def fun3(l,d):
  n = len(l)
  reverse(l,0,d-1)
  reverse(l,d,n-1)
  reverse(l,0,n-1)
  return l

l = [1,2,3,4,5]
i = int(input('Enter number of rotations : '))
# print(fun(l,i))
# print(fun1(l,i))
# print(fun2(l,i))
print(fun3(l,i))