class Node:
  def __init__(self, data, link=None):
    self.data=data
    self.link=link

class LinkedList:
  def __init__(self, n):
    self.head=Node(1)
    node=self.head
    for i in range(2, n+1):
      node.link=Node(i)
      node=node.link
    
  def display(self):
    ptr=self.head
    for _ in range(10):
      print(ptr.data)
      ptr=ptr.link


  def cut(self, fm, to, index):
    startIndex=1
    startNode=self.head
    while startIndex!=fm:
      startIndex+=1
      before=startNode
      startNode=startNode.link
    endIndex=startIndex
    endNode=startNode
    mass=startNode
    while endIndex!=to:
      endIndex+=1
      endNode=endNode.link
    if startIndex==1:
      self.head=endNode.link
    else:
      before.link=endNode.link
    
    insert=self.head
    if index==0:
      endNode.link=self.head
      self.head=mass
    else:
      for _ in range(index-1):
        insert=insert.link
      endNode.link=insert.link
      insert.link=mass
      

    
n=list(map(int, input().split()))
li=LinkedList(n[0])
inst=[]

for _ in range(n[1]):
  inst.append(list(map(int, input().split())))

for i in range(n[1]):
  li.cut(inst[i][0], inst[i][1], inst[i][2])

li.display()