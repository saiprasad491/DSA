
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

def swap_diagonal(L):
  n = len(L)
  for i in range(n):
    L[i][i],L[i][n-1-i] = L[i][n-1-i],L[i][i]
  return L

r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix = read(r,c)
print("matrix : ")
display(matrix)
print("Diagonal elements swapping ")
display(swap_diagonal(matrix))