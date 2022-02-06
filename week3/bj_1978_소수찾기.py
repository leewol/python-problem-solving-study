### 1978 소수 찾기

# 에라토스테네스의 체
# 에라토스테네스의 체는 가장 먼저 소수를 판별할 범위만큼 배열을 할당하여, 해당하는 값을 넣어주고, 이후에 하나씩 지워나가는 방법을 이용한다.

# 1. 배열을 생성하여 초기화한다.
# 2. 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지운다.(지울 때 자기자신은 지우지 않고, 이미 지워진 수는 건너뛴다.)

n = int(input())
n_list = list(map(int, input().split()))

# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
m = int(1000 ** 0.5)

sifter = [True for x in range(1001)] # 1
sifter[0] = 0 # 0은 0으로 처리
sifter[1] = False # 1은 False

for i in range(2, m+1):
  if sifter[i] == True:
    for j in range(i*2, 1001, i): # 2
      sifter[j] = False

count = 0

for num in n_list:
  if sifter[num] == True:
    count += 1

print(count)