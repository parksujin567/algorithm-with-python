n, k=map(int, input().split())
coins=[]
for _ in range(n):
  coins.append(int(input()))
coins.reverse()

sum=0
for i in range(n):
  sum+=k//coins[i]
  k%=coins[i]

print(sum)
