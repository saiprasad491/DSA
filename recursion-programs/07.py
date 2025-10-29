def pow(a,b):
  if b==0:
    return 1
  return a*pow(a,b-1)
for i in range(10):
  print(f"2 to the power {i} is {pow(2,i)}")
print(f"0 to the power 2 is {pow(0,2)}")
