### 11047 동전0
import sys

input = sys.stdin.readline

N, coin_sum = map(int, input().split())
coins = []
count = 0

# 만들어야 하는 합보다 작거나 같은 것들만 넣기
for _ in range(N):
  coin = int(input())
  if coin <= coin_sum:
    coins.append(coin)

for i in range(len(coins)-1, -1, -1):
  if coin_sum == 0:
    break
  count += coin_sum // coins[i]
  coin_sum %= coins[i]

print(count)