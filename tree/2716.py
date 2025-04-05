class Node:
  def __init__(self, elem=None, left=None, right=None):
    self.data=elem
    self.left=left
    self.right=right
  
class Tree:
  def __init__(self):
    self.root=Node("root")
    
n=int(input())
inst=[]
for _ in range(n):
  inst.append(input())

for i in range(n):
  if len(inst[i])==0:
    print(1)
  else: print(len(inst[i]))


