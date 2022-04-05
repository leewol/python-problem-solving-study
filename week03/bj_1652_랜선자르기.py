### 1652 랜선 자르기
import sys
input = sys.stdin.readline

# K: 주어진 랜선 수, N: 자른 후 최소 랜선 수
K, N = map(int, input().split()) 
lans = []

for _ in range(K): 
  lans.append(int(input()))

low, high = 0, max(lans) # N의 범위

while low <= high:
    mid = (low + high) // 2
    count = 0

    for lan in lans: 
      count += lan // mid # 총 몇 개로 나눌 수 있는지

    if count >= N: # N개와 같거나 크면 최소값을 mid+1 (오른쪽 탐색)
      low = mid + 1
    else: # N개보다 작으면 최댓값을 mid-1 (왼쪽 탐색)
      high = mid - 1

print(high)