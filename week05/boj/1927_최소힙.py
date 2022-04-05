### 1927 최소 힙

# heapq
# heapq 모듈의 heappop() 함수를 이용하여 힙에서 원소를 삭제할 수 있습니다. 원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴합니다.

import heapq
import sys

input = sys.stdin.readline
N = int(input())
nums = []

for _ in range(N):
  x = int(input())
  
  if x == 0:
    if not nums:
      print(0)
    else:
      print(heapq.heappop(nums))
  else:
    heapq.heappush(nums, x) # heap에 원소 추가
