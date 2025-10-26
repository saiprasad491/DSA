
def read(r,c):
  L = []
  print(f"Enter {r*c} elements ")
  for i in range(r):
    m = [int(i) for i in input().split()]
    L.append(m)
  return L
def display(L):
  for i in range(len(L)):
    for j in range(len(L[i])):
      print(L[i][j],end=" ")
    print()

def isIdentity(L):
  for i in range(len(L)):
    for j in range(len(L[i])):
      if i==j and L[i][j]!=1 or  i!=j and L[i][j]!=0:
        return "No"
  return "Yes"

r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix = read(r,c)
display(matrix)
print(f"Is given matrix is a identity matrix ? {isIdentity(matrix)}")