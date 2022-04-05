### 11727 2xn 타일링 2

dp = [0 for _ in range(1001)]
dp[1], dp[2] = 1, 3

for i in range(3, 1001):
  dp[i] = 2 * dp[i-2] + dp[i-1]

n = int(input())
print(dp[n] % 10007)