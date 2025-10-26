
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

def swap_row(L,r1,r2):
  for i in range(len(L[0])):
    L[r1][i],L[r2][i] = L[r2][i],L[r1][i]
  return L

r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix = read(r,c)
print("matrix : ")
display(matrix)
r1 = int(input("Enter row 1 : "))
r2 = int(input("Enter row 2 : "))
display(swap_row(matrix,r1,r2))