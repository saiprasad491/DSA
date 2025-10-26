
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

def diagonal_sum(L):
  s = 0
  for i in range(len(L)):
    for j in range(len(L[i])):
      if i==j:
        s += L[i][j]
  return s
def diagonal_sum_both(L):
  e,o = 0,0
  n = len(L)//2
  for i in range(len(L)):
    for j in range(len(L[i])):
      if i==j :
        e += L[i][j]
      if i==len(L)-1-j :
        o += L[i][j]
  return e + o - L[n][n]

r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix1 = read(r,c)
print("Matrix 1 = ")
display(matrix1)
print(f"sum of diagonal elements = {diagonal_sum(matrix1)}")
print(f"sum of diagonals elements = {diagonal_sum_both(matrix1)}")