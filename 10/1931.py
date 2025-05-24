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
    if arr[j][1]>pibot: continue
    else:
      if (arr[j][1]==arr[end][1]) and (arr[j][0]>arr[end][0]): continue
      i+=1
      (arr[i], arr[j])=(arr[j], arr[i])
  (arr[end], arr[i+1])=(arr[i+1], arr[end])
  return i+1

def quickSort(arr, start, end):
  if start<=end:
    pi=Sort(arr, start, end)
    quickSort(arr, start, pi-1)
    quickSort(arr, pi+1, end)

n=int(input())
meeting=[]
sum=0
finish=0
for _ in range(n):
  i=list(map(int, input().split()))
  i.append(i[1]-i[0])
  meeting.append(i)

quickSort(meeting, 0, n-1)

sum+=1
finish=meeting[0][1]

i=1
while i<n:
  if meeting[i][0]<finish:
    i+=1
  else:
    sum+=1
    finish=meeting[i][1]

print(sum)
