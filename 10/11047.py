inst=list(map(int, input().split()))
coins=[]
sum=0
for _ in range(inst[0]):
  coins.append(int(input()))

i=len(coins)
while i!=0:
  i-=1
  sum+=inst[1]//coins[i]
  inst[1]%=coins[i]

print(sum)