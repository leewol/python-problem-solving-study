### 11286 절댓값 힙
# 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성
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
      continue

    out = heapq.heappop(nums)
    if out[1] == False:
      print(-out[0])
    else:
      print(out[0])
  else:
    if x < 0:
      heapq.heappush(nums, (abs(x), False))
    elif x > 0:
      heapq.heappush(nums, (abs(x), True))
