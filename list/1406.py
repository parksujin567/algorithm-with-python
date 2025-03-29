class DNode:
  def __init__(self, elem, prev=None, next=None):
    self.data=elem
    self.prev=prev
    self.next=next


class DbLinkedList:
  def __init__(self, str):
    node=DNode(str[0])
    self.head=node
    for i in range(len(str)-1):
      node.next=DNode(str[i+1])
      node.next.prev=node
      node=node.next
    node.next=DNode('Fin')
    node.next.prev=node
    self.cursor=node.next

  def functionL(self):
    if self.cursor.prev!=None:
      self.cursor=self.cursor.prev

  def functionD(self):
    if self.cursor.next!=None:
      self.cursor=self.cursor.next

  def functionB(self):
    if self.cursor.prev!=None:
      before=self.cursor.prev
      if before.prev==None:
        self.head=self.cursor
        self.cursor.prev=None
      else:
        before.prev.next=self.cursor
        self.cursor.prev=before.prev

  def functionP(self, e):
    node=DNode(e)
    if self.cursor.prev==None:
      node.next=self.cursor
      self.cursor.prev=node
      self.head=node
    else:
      node.next=self.cursor
      node.prev=self.cursor.prev
      self.cursor.prev=node
      node.prev.next=node

  def display(self):
    ptr=self.head
    
    while ptr.data!='Fin':
      print(ptr.data, end="")
      ptr=ptr.next


str=input()
li=DbLinkedList(str)
n=int(input())
for _ in range(n):
  inst=input().split()
  if inst[0]=='L':
    li.functionL()
  elif inst[0]=='D':
    li.functionD()
  elif inst[0]=='B':
    li.functionB()
  elif inst[0]=='P':
    li.functionP(inst[1])


li.display()