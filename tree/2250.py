from collections import defaultdict

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

  def makeTree(self, arr):
    for i in range(len(arr)):
      node=self.search(arr[i][0])
      if node==None: node=self.root
      if arr[i][1]!=-1:
        node.left=Node(arr[i][1])
      if arr[i][2]!=-1:
        node.right=Node(arr[i][2])

  def inorder(self, arr, node=None, level=0):
    if node==None: node=self.root
    if node.left!=None:self.inorder(arr, node.left, level+1)
    arr.append(level)
    if node.right!=None: self.inorder(arr, node.right, level+1)

n=int(input())
arr=[]
for _ in range(n):
  arr.append(list(map(int, input().split())))

t=Tree()
t.makeTree(arr)
result=[-1]

t.inorder(result)

width=defaultdict(list)
for idx, level in enumerate(result, start=1):
  width[level].append(idx)

max_width=0
max_level=0
for lvl in sorted(width.key()):
  indices=width[lvl]
  wid=indices[-1]-indices[0]+1
  if wid >max_width:
    max_width=wid
    max_level=lvl

print(max_level, max_width)