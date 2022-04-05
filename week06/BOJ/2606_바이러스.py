### 2606 바이러스
import sys

input = sys.stdin.readline
n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결된 컴퓨터 쌍 수
v = 1
graph = {}

def dfs(graph, start, visited = []):
  visited.append(start)

  for node in graph[start]:
    if node not in visited:
      dfs(graph, node, visited)
  return visited

for i in range(1, n+1):
  graph[i] = []

for _ in range(m):
  x, y = map(int, input().split())

  graph[x].append(y)
  graph[y].append(x)

for node, go in graph.items():
  go.sort()

result = dfs(graph, v)

print(len(result) - 1)