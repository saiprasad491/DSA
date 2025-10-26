import random
def fun():
  L=[]
  for i in range(10):
    L.append(random.randint(1,20))
  return L
print(fun())

