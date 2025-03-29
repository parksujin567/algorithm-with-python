n=int(input())
str=[]
stack=[]
top=-1

def push(x):
  global top, stack
  top+=1
  stack.append(x)

def pop():
  global top, stack
  top-=1
  if top==-1:
    print(stack.pop())
  else:
    print(stack.pop(), end=" ")


for i in range(0, n):
  str.append(input().split())

for i in range(0, n):
  for s in str[i]:
    push(s)
  print("Case #%d:" %(i+1), end=" ")
  for _ in range(0, len(str[i])):
    pop()
