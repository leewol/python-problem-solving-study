### 2775 부녀회장이 될 테야
cases = int(input())

for _ in range(cases):
  k = int(input()) # 층
  n = int(input()) # 호
  floor = [x for x in range(1, n+1)] # 0층 n호까지 초기화
  
  for i in range(k): # k-1번 만큼 반복
    for j in range(1, n):
      floor[j] += floor[j-1] # 호실 사람 수 계속해서 더해 주기

  print(floor[-1])