### 1259 팰린드롬수
while True:
  num = input()
  answer = 'yes'

  if num == '0':
    break
  
  for i in range(len(num) // 2):
    if num[i] != num[-(i+1)]:
      answer = 'no'

  print(answer)