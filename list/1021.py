class DNode:
  def __init__(self, elem, prev=None, next=None):
    self.data=elem
    self.prev=prev
    self.next=next

class DbLinkedList:
  def __init__(self, n):
    self.size=n
    self.count=0
    self.head=DNode(1)
    node=self.head
    for i in range(2, n+1):
      node.next=DNode(i)
      node.next.prev=node
      node=node.next
    self.last=node

  def delete(self):
    if self.size==1:
      self.head==None
    else:
      self.head=self.head.next
      self.head.prev=None
      self.size-=1

  def moveLeft(self):
    node=self.head #움직이는 노드
    self.last.next=node #마지막노드 넥스트-> 새로운 노드드
    self.head=self.head.next  #머리노드 next
    self.head.prev=None #새로운 머리노드의 prev None
    node.prev=self.last #새로운 노드 prev->꼬리 노드
    self.last=self.last.next #꼬리노드 변경경
    node.next=None
    self.count+=1

  def moveRight(self):
    node=self.last
    self.last=self.last.prev
    self.last.next=None
    node.next=self.head
    node.prev=None
    self.head.prev=node
    self.head=node
    self.count+=1

  def operation(self, n):
    index=1
    node=self.head
    while node.data!=n:
      index+=1
      node=node.next
    if index-1<=self.size-index:
      for _ in range(index-1):
        self.moveLeft()
    else:
      for _ in range(self.size-index+1):
        self.moveRight()
    self.delete()

n=int(input().split()[0])
inst=list(map(int, input().split()))
li=DbLinkedList(n)
for i in range(len(inst)):
  li.operation(inst[i])

print(li.count)

