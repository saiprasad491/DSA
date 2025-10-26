
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

def transpose(L):
  for i in range(len(L)):
    for j in range(len(L[i])):
      if i<j:
        L[i][j],L[j][i] = L[j][i],L[i][j]

def reverse(L):
  for i in range(len(L)):
    L[i].reverse()

def rotate_matrix(L):
  transpose(L)
  reverse(L)
  return L
r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix = read(r,c)
print("Given matrix ")
display(matrix)
print("Rotating matrix by 90 degrees : ")
display(rotate_matrix(matrix))