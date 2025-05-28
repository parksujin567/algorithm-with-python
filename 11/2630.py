def dividedmat(mat, startr, startc, endr, endc):
  global white, blue
  result=is_one(mat, startr, startc, endr, endc)
  if result=="white": white+=1
  elif result=="blue": blue+=1
  else:
    dividedmat(mat, startr, startc, (endr+startr)//2, (endc+startc)//2)
    dividedmat(mat, startr, (endc+startc)//2+1, (endr+startr)//2, endc)
    dividedmat(mat, (endr+startr)//2+1, startc, endr, (endc+startc)//2)
    dividedmat(mat, (endr+startr)//2+1, (endc+startc)//2+1, endr, endc)

def is_one(mat, startr, startc, endr, endc):
  c=mat[startr][startc]
  for i in range(startr, endr+1):
    for j in range(startc, endc+1):
      if mat[i][j]!=c:
        return False
  if c==0: return "white"
  else: return "blue"

k=int(input())
mat=[]
white, blue=0, 0
for _ in range(k):
  mat.append(list(map(int, input().split())))

dividedmat(mat, 0, 0, k-1, k-1)
print(white)
print(blue)