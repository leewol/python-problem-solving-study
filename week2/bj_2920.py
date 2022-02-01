### 2920 음계

num_list = list(map(int, input().split()))
answer = 'mixed'

if num_list[0] == 1:
  for i in range(2, 9):
    if num_list[i-1] == i:
      answer = 'ascending'
    else:
      answer = 'mixed'
      break
elif num_list[0] == 8:
  for i in range(2, 9):
    if num_list[i-1] == 9-i:
      answer = 'descending'
    else:
      answer = 'mixed'
      break

print(answer)