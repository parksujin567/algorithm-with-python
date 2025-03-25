N=int(input())+1
front=0 
rear=0
queue=[None]*N
card=[]

def enqueue(x):
  global front, rear, card, queue
  rear=(rear+1)%N
  queue[rear]=int(x)

def discard(): #버리기기
  global front, rear, card, queue
  front=(front+1)%N
  card.append(queue[front])
  queue[front]=None

def back(): #뒤로보내기기
  global front, rear, card, queue
  front=(front+1)%N
  enqueue(queue[front])
  queue[front]=None
  

for i in range(0, N-1): #기본셋팅팅
  enqueue(i+1)

count=0
while (rear-front+N)%N!=1:
  if count%2==0:
    discard()
  else:
    back()
  count+=1

for i in range(0, N-2):
  print(card[i], end=" ")

print(queue[rear])