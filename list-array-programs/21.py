
def fun(l):
  n = len(l)
  for i in range(0,n):
    c = 1
    for j in range(i+1,n):
      if l[i]==l[j]:
        c += 1
    if c>n//2:
      # return l[i]
      return i
  return -1

l = [8,3,4,8,8]
print(f"position of majority element {fun(l)}")
print(f"position of majority element {fun([8,7,6,8,6,6,6,6])}")
print(f"position of majority element {fun([3,4,7,7,7,5])}")