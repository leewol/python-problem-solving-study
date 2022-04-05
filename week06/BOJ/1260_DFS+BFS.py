### 1260 DFS와 BFS
import sys

input = sys.stdin.readline
graph = {}

# DFS
def dfs(graph, start, visited = []):
  visited.append(start)
 
  for node in graph[start]:
    if node not in visited:
      dfs(graph, node, visited)
  return visited

# BFS
def bfs(graph, start):
  need_visited, visited = [], []
  need_visited.append(start)
    
  while need_visited:
    node = need_visited[0]
    del need_visited[0]
        
    if node not in visited:
      visited.append(node)
      need_visited.extend(graph[node])
  return visited
  
# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

# 간선이 연결하는 두 정점의 번호 입력받기
for i in range(1, N+1):
  graph[i] = []

for _ in range(M):
  x, y = map(int, input().split())

  graph[x].append(y)
  graph[y].append(x)

for node, go in graph.items():
  go.sort()

print(*dfs(graph, V))
print(*bfs(graph, V))