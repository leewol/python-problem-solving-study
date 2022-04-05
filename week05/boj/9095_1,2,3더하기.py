### 9095 1,2,3 더하기
import sys
input = sys.stdin.readline

sum_cases = [0 for _ in range(11)]
sum_cases[1] = 1
sum_cases[2] = 2
sum_cases[3] = 4

for i in range(4, 11):
  sum_cases[i] = sum_cases[i-1] + sum_cases[i-2] + sum_cases[i-3]

t = int(input())
for _ in range(t):
  n = int(input())
  print(sum_cases[n])