### 2562 최댓값
num_list = []
for i in range(0, 9):
  num_list.append(int(input()))

max_num = max(num_list)
print(max_num)
print(num_list.index(max_num)+1)

