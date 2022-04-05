### 2579 계단 오르기
import sys

input = sys.stdin.readline

stairs = int(input())
dp = [0 for _ in range(301)]
score = [0 for _ in range(301)]

for i in range(stairs):
  score[i] = int(input())

dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0] + score[2], score[1] + score[2])

# 마지막 계단 직전 계단을 밟거나, 밟지 않거나
for i in range(3, stairs):
  dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])

print(dp[stairs-1])