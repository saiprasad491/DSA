
def fun(L):
  if len(L)==0: return 0.0
  s = 0
  for i in L:
    s += i
  return s/len(L)
def fun1(L):
  if len(L)==0: return 0.0
  return sum(L)/len(L)

L = [1,2,3,4,5]
print(f"List={L} and average = {fun(L)}")
print(f"List={[]} and average = {fun1([])}")