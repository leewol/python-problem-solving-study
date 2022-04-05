### 11279 최대 힙 - 마이너스해서 넣어주면 최소가 됨
import sys
import heapq

input = sys.stdin.readline
N = int(input())
nums = []

for _ in range(N):
  x = int(input())
  
  if x == 0:
    if not nums:
      print(0)
    else:
      print(heapq.heappop(nums) * (-1))
  else:
    heapq.heappush(nums, -x)
