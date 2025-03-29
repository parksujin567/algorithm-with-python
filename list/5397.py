class DNode:
  def __init__(self, elem, prev=None, next=None):
    self.data=elem
    self.prev=prev
    self.next=next


class DbLinkedList:
  def __init__(self):
    self.head=DNode('Fin')
    self.cursor=self.head

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
    print("")

n=int(input())
str=[]
li=[]
for _ in range(n):
  str.append(input())
  li.append(DbLinkedList())

for i in range(len(str)):
  for j in range(len(str[i])):
    if str[i][j]=='-':
      li[i].functionB()
    elif str[i][j]=='<':
      li[i].functionL()
    elif str[i][j]=='>':
      li[i].functionD()
    else:
      li[i].functionP(str[i][j])

for i in range(len(li)):
  li[i].display()