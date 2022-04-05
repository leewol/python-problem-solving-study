### 1165 구간 합 구하기 4 --> Prefix Sum
import sys

input = sys.stdin.readline

# 수의 개수 N, 합을 구해야하는 횟수 M
N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [nums[0]]

for i in range(1, N):
  prefix_sum.append(prefix_sum[i-1] + nums[i]) 

for _ in range(M):
  i, j = map(int, input().split())
  if i == 1:
    answer = prefix_sum[j-1]
  else:
    answer = prefix_sum[j-1] - prefix_sum[(i-1)-1]

  print(answer)