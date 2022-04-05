### 1003 피보나치 함수
d = [[1, 0], [0, 1]]

for i in range(2, 41):
  d.append([ d[i-2][0] + d[i-1][0], d[i-2][1] + d[i-1][1] ])

t = int(input())

for _ in range(t):
  num = int(input())
  print(f'{d[num][0]} {d[num][1]}')