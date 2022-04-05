### 7568 덩치
# 무식하게 ,, 다 보는 방법,,
cases = int(input())
cases_arr = []
ranking = 1

for _ in range(cases):
  w, h = map(int, input().split())
  cases_arr.append([w, h])

for i in range(cases):
  for j in range(cases):
    if i != j:
      if cases_arr[i][0] < cases_arr[j][0] and cases_arr[i][1] < cases_arr[j][1]:
        ranking += 1
  cases_arr[i].append(ranking)
  ranking = 1

for i in range(cases):
  print(cases_arr[i][2], end=' ')