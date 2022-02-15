### 1966 프린터 큐
import sys

input = sys.stdin.readline
cases = int(input())

for _ in range(cases):
  N, M = map(int, input().split()) # 문서 수, 인쇄할 문서
  p = list(map(int, input().split())) # 문서들 우선순위

  new_p = []
  for i in range(N):
    if i == M:
      new_p.append([p[i], True])
    else:
      new_p.append([p[i], False])

  count = 1 # 몇 번째에 인쇄되는지
  target = new_p[M] # 인쇄할 문서의 정보

  while p:
    if new_p[0][0] == max(p):
      if new_p[0][1] == True:
        print(count)
        break
      new_p.pop(0)
      p.pop(0)
      count += 1
    else:
      tmp = p.pop(0)
      tmp2 = new_p.pop(0)
      p.append(tmp)
      new_p.append(tmp2)