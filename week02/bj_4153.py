### 4153 직각삼각형 --- math.pow, math.sqrt / 원하는 값 제거 == .remove()
import math

while True:
  lines = list(map(int, input().split()))
  c = max(lines)
  lines.remove(c)
  a = lines[0]
  b = lines[1]

  if a==0 and b==0 and c==0:
    break
  
  if c == math.sqrt(math.pow(a, 2) + math.pow(b, 2)):
    print("right")
  else:
    print("wrong")