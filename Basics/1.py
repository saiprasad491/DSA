#WAP to capitalize alternate character of a string.
def myFun(str):
  li = list(str)
  ll = []
  for i in range(len(li)):
    if(i%2==0):
      ll.append(li[i].upper())
    else:
      ll.append(li[i])
  return ''.join(ll)
str = input('Enter any string ')
print(myFun(str))