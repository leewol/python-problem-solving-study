### 11720 숫자의 합
size = int(input())
num_str = input()
sum = 0

for i in range(size):
  sum += int(num_str[i])

print(sum)