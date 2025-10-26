
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
def sum(L,M):
  r1,c1,r2,c2 = len(L),len(L[0]),len(M),len(M[0])
  if r1==r2 and c1==c2:
    for i in range(r1):
      for j in range(c1):
        L[i][j] += M[i][j]
    return L
  else:
    print("Can't find sum")
r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix1 = read(r,c)
r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix2 = read(r,c)
print("Matrix 1 = ")
display(matrix1)
print("Matrix 2 = ")
display(matrix2)
print("Sum of Matrix 1 and Matrix 2 = ")
display(sum(matrix1,matrix2))