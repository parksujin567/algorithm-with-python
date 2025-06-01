def dividedmat(mat, startr, startc, endr, endc):
  result=is_one(mat, startr, startc, endr, endc)
  if result==0: return "0"
  elif result==1: return "1" 
  else:
    midr=(startr+endr)//2
    midc=(startc+endc)//2
    return ("("+
    dividedmat(mat, startr, startc, midr, midc)+
    dividedmat(mat, startr, midc+1, midr, endc)+
    dividedmat(mat, midr+1, startc, endr, midc)+
    dividedmat(mat, midr+1, midc+1, endr, endc)+")")

def is_one(mat, startr, startc, endr, endc):
  c=mat[startr][startc]
  for i in range(startr, endr+1):
    for j in range(startc, endc+1):
      if mat[i][j]!=c:
        return -1
  return c

n=int(input())
mat=[]
for _ in range(n):
  mat.append(list(map(int, input().strip())))

ans=dividedmat(mat, 0, 0, n-1, n-1)
print(ans)