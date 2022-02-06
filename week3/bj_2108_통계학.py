### 2108 통계학 ----------- Python3 시간 초과 (pypy3으로 제출)
from collections import Counter

N = int(input()) # 수의 개수 N은 홀수
n_list = []

for _ in range(N):
  n_list.append(int(input()))

n_list.sort() # 오름차순 정렬

# 평균
mean = round(sum(n_list) / N) 

# 중앙값
median = n_list[N//2] 

# 빈도 높은 것 내림차순 / 값 크기 오름차순
freq = sorted(Counter(n_list).items(), key=lambda x:(-x[1], x[0]))
# 10
# 8
# 8
# 4
# 9
# 9
# 1
# 5
# 1
# 2
# 2
# [(1, 2), (2, 2), (8, 2), (9, 2), (4, 1), (5, 1)]

# 최빈값
if len(freq) != 1 and freq[0][1] == freq[1][1]:
  mode = freq[1][0]
else:
  mode = freq[0][0]

# 범위
n_range = n_list[N-1] - n_list[0]  

print(f'{mean}\n{median}\n{mode}\n{n_range}')