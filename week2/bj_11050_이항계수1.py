# --------------팩토리얼 생각해 보기

## 11050 이항 계수 1
import math

N, K = map(int, input().split())
result = math.factorial(N) / (math.factorial(K) * math.factorial(N-K))

print(int(result))