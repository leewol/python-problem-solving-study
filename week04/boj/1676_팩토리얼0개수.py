### 1676 팩토리얼 0의 개수
N = int(input())
count = 0

# factorial
def factorial(num):
  if num > 1:
    return num * factorial(num-1)
  else:
    return 1

N_fac = str(factorial(N))

for i in range(len(N_fac)-1, -1, -1):
  if N_fac[i] != '0':
    break
  count += 1

print(count)