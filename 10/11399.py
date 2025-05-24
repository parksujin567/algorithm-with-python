def Sort(arr, start, end):
  mid=(start+end)//2
  a=arr[start]
  b=arr[mid]
  c=arr[end]
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
    if arr[j]<pibot:
      i+=1
      arr[i], arr[j]=arr[j], arr[i]
  arr[i+1], arr[end]=arr[end], arr[i+1]
  return i+1

def quickSort(arr, start, end):
  if start<end:
    pi=Sort(arr, start, end)
    quickSort(arr, start, pi-1)
    quickSort(arr, pi+1, end)

n=int(input())
time=list(map(int, input().split()))

quickSort(time, 0, n-1)

sum=0
i=n
c=1
while i!=0:
  i-=1
  sum+=time[i]*c
  c+=1
print(sum)