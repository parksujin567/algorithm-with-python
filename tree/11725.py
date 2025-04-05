class Node:
  def __init__(self, elem, left=None, right=None):
    self.data=elem
    self.left=left
    self.right=right
  
class Tree:
  def __init__(self):
    self.root=Node(1)

  def search(self, elem, node=None):
    if node==None:
      node=self.root
    if node.data==elem:
      return node
    if node.left!=None:
      found=self.search(elem, node.left)
      if found: return found
    if node.right!=None:
      found=self.search(elem, node.right)
      if found: return found
    return None
  
  def makeNode(self, elem, before=None):
    if before==None:
      before=self.root
    if before.left==None:
      before.left=Node(elem)
    elif before.right==None:
      before.right=Node(elem)


n=int(input())
inst=[]
t=Tree()
for _ in range(n-1):
  inst.append(list(map(int, input().split())))
maked=[1]
parents=[]

for st, nd in inst:
  if st in maked:
    node=t.search(st)
    t.makeNode(nd)
    maked.append(nd)
    parents.append([nd, st])
  elif nd in maked:
    node=t.search(nd)
    t.makeNode(st)
    maked.append(st)
    parents.append([st, nd])

result=[None]*(n+1)
for data, parent in parents:
  result[data]=parent

for i in range(2, n+1):
  print(result[i])

