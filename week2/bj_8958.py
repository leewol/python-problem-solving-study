### 8958 OX퀴즈
for i in range(int(input())):
  combo = 0
  result = 0

  for j in input():
    if j == 'O':
      result += (combo + 1)
      combo += 1
    else:
      combo = 0

  print(result)