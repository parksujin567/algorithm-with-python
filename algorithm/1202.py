def Sort(arr, start, end):
  mid=(start+end)//2
  a=arr[start][1]
  b=arr[mid][1]
  c=arr[end][1]
  if (a-b)*(c-a)>0:
    pibot=a
    pibot_idx=start
  elif (b-c)*(a-b)>0:
    pibot=b
    pibot_idx=mid
  else:
    pibot=c
    pibot_idx=end
  (arr[end], arr[pibot_idx])=(arr[pibot_idx], arr[end])
  i=start-1
  for j in range(start, end):
    if arr[j][1]<pibot:
      i+=1
      arr[i], arr[j]=arr[j], arr[i]
  arr[i+1], arr[end]=arr[end], arr[i+1]
  return i+1

def quickSort(arr, start, end):
  if start<end:
    pi=Sort(arr, start, end)
    quickSort(arr, start, pi-1)
    quickSort(arr, pi+1, end)

n, k=map(int, input().split())
jewel=[]
for _ in range(n):
  i=
  jewel.append(list(map(int, input().split())))
weight=int(input())

quickSort(jewel, 0, n-1)

cost=[]
c=0
i=n-1
while c<k or i>=0:
  if jewel[i][0]<=weight:
    cost+=jewel[i][1]
    c+=1
  i-=1
print(cost)