class Node:                                        #노드 클래스, 데이터와 링크를 가짐, 링크가 매개변수로 주어지지 않는 경우 None
  def __init__(self, data, link=None):
    self.data = data
    self.link = link

def printList(head):                               #리스트 출력함수
  ptr=head
  while ptr.link!=None:
    print(ptr.data, end=" -> ")
    ptr=ptr.link
  print(ptr.data)

def arrayList(array):                              #배열을 연결리스트로 만드는 함수수
  head=None
  for i in array:
    if head==None:
      new=Node(i)
      head=new
    else:
      new.link=Node(i)
      new=new.link
  return head

def mergeSort(head):
  if not head or not head.link:                  #노드가 하나밖에 없거나 아예 없으면 head(가장 첫번째 노드를 가리키는 변수수) 반환환
    return head

  def split(head):                               #연결리스트를 절반으로 나누는 함수수
    i, j = head, head.link
    while j and j.link:                        #j가 i보다 두배 더 빠르게 이동하면서 중간인덱스를 얻을 수 있다.
      i = i.link
      j=j.link.link
    middle = i.link
    i.link = None
    return head, middle

  def merge(l1, l2):                             #정렬된 두 리스트를 병합하는 함수수
    start = Node("s")                          #병합된 리스트의 처음을 가리킴. l2가 l1보다 작으면 l1왼쪽에 삽입해야 되기 때문에 빈노드 필요요
    tail = start                               #병합된 리스트의 마지막 노드를 가리키는 변수
    while l1 and l2:
      if l1.data < l2.data:
        tail.link = l1                     #병합된 리스트에 l1연결결
        l1 = l1.link                       #l1 오른쪽으로 옮김
      else:
        tail.link = l2                     #l2연결
        l2 = l2.link                       #l2 오른쪽으로 옮김
      tail = tail.link                       #새롭게 연결한 노드로 tail 옮기기
    tail.link = l1 if l1 else l2               #한쪽 리스트를 다 옮기고 나머지 리스트 다 옮기기
    return start.link                          #빈노드를 제외하고 병합된 리스트를 반환

  left, right = split(head)                      
  left = mergeSort(left)
  right = mergeSort(right)
  return merge(left, right)


arr1=[3, 6, 9, 2, 6, 9]
li1=arrayList(arr1)
printList(li1)
li1=mergeSort(li1)
printList(li1)