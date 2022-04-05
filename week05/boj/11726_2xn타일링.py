### 11726 2xn 타일링 == 1, 2로 n 만들기

n = int(input()) # 2xn의 n
dp = [0 for _ in range(1001)]
dp[1], dp[2] = 1, 2

for i in range(3, 1001):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)