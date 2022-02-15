### 1929 소수 구하기
M, N = map(int, input().split())

# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
n = int(N ** 0.5)

sifter = [True for x in range(N+1)]
sifter[0] = 0 # 0은 0으로 처리
sifter[1] = False # 1은 False

for i in range(2, n+1):
  if sifter[i] == True:
    for j in range(i*2, N+1, i):
      sifter[j] = False

for num in range(M, N+1):
  if sifter[num] == True:
    print(num)