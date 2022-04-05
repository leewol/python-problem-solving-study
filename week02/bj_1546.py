### 1546 평균
nums = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
sum = 0

for score in scores:
  sum += score / max_score * 100

print(sum / nums)