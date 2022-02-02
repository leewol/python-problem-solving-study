### 2798 블랙잭
N, M = map(int, input().split()) # 카드 개수, 기준 수
card_nums = list(map(int, input().split())) # 카드에 적힌 숫자들
max_num = 0

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      summ = card_nums[i] + card_nums[j] + card_nums[k]

      if summ <= M and summ > max_num:
        max_num = summ

print(max_num)