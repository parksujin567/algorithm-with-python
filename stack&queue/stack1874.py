n=int(input())
stack=[]
top=-1
cal=[]
arr=[] #수열

def push(x):
  global top, stack, cal
  top+=1
  stack.append(int(x))
  cal.append("+")

def pop():
  global top, stack, cal
  stack.pop()
  top-=1
  cal.append("-")

count=1
for _ in range(0, n):
  arr.append(int(input()))

for i in arr:
  while True:
    if (stack and i>stack[top]) or top==-1:
      push(count)
      count+=1
    elif stack and i==stack[top]:
      pop()
      break
    else:
      print("NO")
      exit()

for j in cal:
  print(j)