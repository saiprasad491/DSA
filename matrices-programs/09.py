
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

def opposite_diagonal_sum(L):
  s = 0
  for i in range(len(L)):
    for j in range(len(L[i])):
      if i==len(L)-1-j:
        s += L[i][j]
  return s
r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix1 = read(r,c)
print("Matrix 1 = ")
display(matrix1)
print(f"sum of diagonal elements = {opposite_diagonal_sum(matrix1)}")