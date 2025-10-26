
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
def row_wise(L):
  ans=[]
  for i in range(len(L)):
    ans.append(sum(L[i]))
  return ans
r = int(input('Enter row number : '))
c = int(input('Enter column number : '))
matrix1 = read(r,c)
print("Matrix 1 = ")
display(matrix1)
print(f"Row wise sum of Matrix 1  = {row_wise(matrix1)}")