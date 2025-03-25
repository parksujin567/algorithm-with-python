stack=[]
top=-1

def push(x):
  global top, stack
  top+=1
  stack.append(x)

def pop():
  global top, stack
  if top!=-1:
    print(stack.pop())
    top-=1
  else:
    print(-1)  

def size():
  print(top+1)

def empty():
  if top==-1:
    print(1)
  else:
    print(0)
  
def funcTop():
  if top==-1:
    print(-1)
  else:
    print(stack[top])

N=int(input())

for i in range(0, N):
  inst=input().split()
  if inst[0]=='push':
    push(inst[1])
  elif inst[0]=='top':
    funcTop()
  elif inst[0]=='size':
    size()
  elif inst[0]=='pop':
    pop()
  else:
    empty()