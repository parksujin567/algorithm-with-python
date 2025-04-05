class Node:
  def __init__(self, elem, left=None, right=None):
    self.data=elem
    self.left=left
    self.right=right
  
class Tree:
  def __init__(self):
    self.root=Node('A')

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
      if arr[i][1]!='.':
        node.left=Node(arr[i][1])
      if arr[i][2]!='.':
        node.right=Node(arr[i][2])

  def preorder(self, node=None):
    if node==None: node=self.root
    print(node.data, end="")
    if node.left!=None: self.preorder(node.left)
    if node.right!=None: self.preorder(node.right)

  def inorder(self, node=None):
    if node==None: node=self.root
    if node.left!=None:self.inorder(node.left)
    print(node.data, end="")
    if node.right!=None: self.inorder(node.right)
  
  def postorder(self, node=None):
    if node==None: node=self.root
    if node.left!=None:self.postorder(node.left)
    if node.right!=None: self.postorder(node.right)
    print(node.data,end="")
  
n=int(input())
arr=[]
for _ in range(n):
  arr.append(input().split())
tree=Tree()
tree.makeTree(arr)
tree.preorder()
print()
tree.inorder()
print()
tree.postorder()
