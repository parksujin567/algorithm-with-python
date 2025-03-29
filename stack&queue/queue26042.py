info=[]
queue=[]
front=-1
rear=-1
max=0
num=0

def enqueue(x):
  global num, rear, queue
  rear+=1
  queue.append(int(x))

def dequeue():
  global front, queue
  if front!=rear:
    front+=1

def cal():
  global rear, front, max, num, queue
  if rear-front>max:
    max=rear-front
    num=queue[rear]
  elif rear-front==max and (queue[rear]<num):
    num=queue[rear]
  elif num==0:
    num=queue[rear]

n=int(input())
for _ in range(0, n):
  info.append(input().split())

for i in range(0, n):
  if int(info[i][0])==1:
    enqueue(info[i][1])
    cal()
  else:
    dequeue()

print(max, num)