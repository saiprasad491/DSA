
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

def col_wise(L):
  for j in range(len(L[0])):
    s = 0
    for i in range(len(L)):
      s += L[i][j]
    print(f"column {j} sum = {s}")

r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix1 = read(r,c)
print("Matrix 1 = ")
display(matrix1)
col_wise(matrix1)