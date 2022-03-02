### 1389 케빈 베이컨의 6단계 법칙

import sys

input = sys.stdin.readline
N, M = map(int, input().split()) # 유저 수, 친구 관계 수
graph = {}
kevin_bacon = {}

def bfs(graph, start):
  steps = {}
  sum = 0
  
  for i in range(1, N+1):
    steps[i] = [0, False]
  steps[start] = [0, True]
  
  need_visited, visited = [], []
  need_visited.append(start)

  while need_visited:
    node = need_visited[0]
    del need_visited[0]

    if node not in visited:   
      visited.append(node)
      need_visited.extend(graph[node])
      
      for i in need_visited:
        if steps[i][1] == False:
          steps[i] = [steps[node][0]+1, True]
          sum += steps[node][0]+1
  return sum
  
for i in range(1, N+1):
  graph[i] = []

for _ in range(M):
  x, y = map(int, input().split())

  if y not in graph[x]:
    graph[x].append(y)
  if x not in graph[y]:
    graph[y].append(x)

for i in range(1, N+1):
  kevin_bacon[i] = bfs(graph, i)


kevin_bacon = sorted(kevin_bacon.items(), key=lambda x:(x[1], x[0]))

print(kevin_bacon[0][0])