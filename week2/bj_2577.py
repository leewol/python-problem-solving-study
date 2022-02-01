### 2577 숫자의 개수
result = 1
for i in range(3):
  result = result * int(input())

for i in range(0, 10):
  print(str(result).count(f'{i}'))