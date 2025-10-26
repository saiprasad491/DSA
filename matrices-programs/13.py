
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

def swap_col(L,c1,c2):
  for i in range(len(L)):
    L[i][c1],L[i][c2] = L[i][c2],L[i][c1]
  return L

r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix = read(r,c)
print("matrix : ")
display(matrix)
c1 = int(input("Enter column 1 : "))
c2 = int(input("Enter column 2 : "))
display(swap_col(matrix,c1,c2))