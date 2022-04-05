### 1463 1로 만들기
n = int(input())
memoization = [0] * (n+1)

for i in range(2, n+1):
  memoization[i] = memoization[i-1] + 1
  if i % 3 == 0:
    memoization[i] = min(memoization[i], memoization[i//3] + 1)
  if i % 2 == 0:
    memoization[i] = min(memoization[i], memoization[i//2] + 1)

print(memoization[n])