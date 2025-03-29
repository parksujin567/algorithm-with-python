N=int(input())
length=[]
value=0
count=0

def push(x):
  global length
  length.append(x)

for _ in range(0, N):
  push(int(input()))

for i in range(0, N):
  p=length.pop()
  if p>value:
    value=p
    count+=1

print(count)

