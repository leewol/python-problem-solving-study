### 2751 수 정렬하기 2
n = int(input())
num_list = []

for _ in range(n):
  num_list.append(int(input()))

num_list.sort()

for num in range(num_list):
  print(num)