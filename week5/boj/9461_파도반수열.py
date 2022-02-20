### 9461 파도반 수열
import sys
input = sys.stdin.readline

p = [0 for _ in range(101)]
for i in range(1, 101):
  if i < 4:
    p[i] = 1
  else:
    p[i] = p[i-3] + p[i-2]

t = int(input())

for _ in range(t):
  n = int(input())
  print(p[n])