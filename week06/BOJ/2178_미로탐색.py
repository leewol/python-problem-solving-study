### 2178 미로 탐색
from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split()) # N x M 행렬
maze = []

for _ in range(N):
  row = list(map(int, input().rstrip()))
  maze.append(row)

need_visited = deque()
dx = [-1, 0, 1, 0] # 시계방향 확인
dy = [0, 1, 0, -1]

def bfs(x, y):
  need_visited.append({'x': 0, 'y': 0})
  # print(need_visited)
  
  while need_visited:
    cx, cy = need_visited[0]['x'], need_visited[0]['y']
    # print(cx, cy, x, y)
    if cx == x and cy == y:
      break

    need_visited.popleft()

    for i in range(4):
      # print(cx+dx[i], cy+dy[i], maze[cx+dx[i]][cy+dy[i]])
      nx, ny = cx+dx[i], cy+dy[i]
      if 0 <= nx <= x and 0 <= ny <= y:
        if maze[nx][ny] == 1:
          need_visited.append({'x': nx, 'y': ny})
          maze[nx][ny] = maze[cx][cy] + 1
          # print(need_visited)

bfs(N-1, M-1)
print(maze[N-1][M-1])


# -- 1. 시간 초과
# from collections import deque
# import sys

# input = sys.stdin.readline
# N, M = map(int, input().split()) # N x M 행렬
# maze = []

# for _ in range(N):
#   row = list(map(int, input().rstrip()))
#   maze.append(row)

# need_visited = deque()
# visited = [[0 for _ in range(M)] for _ in range(N)]
# dx = [-1, 0, 1, 0] # 시계방향 확인
# dy = [0, 1, 0, -1]

# def bfs(x, y):
#   need_visited.append({'x': 0, 'y': 0, 'd': 1})
#   # print(need_visited)
  
#   while need_visited:
#     cx, cy, cd = need_visited[0]['x'], need_visited[0]['y'], need_visited[0]['d']
#     # print(cx, cy, cd, x, y)
#     if cx == x and cy == y:
#       break

#     need_visited.popleft()
#     visited[cx][cy] = 1

#     for i in range(4):
#       # print(cx+dx[i], cy+dy[i], maze[cx+dx[i]][cy+dy[i]], visited[cx+dx[i]][cy+dy[i]])
#       nx, ny = cx+dx[i], cy+dy[i]
#       if 0 <= nx <= x and 0 <= ny <= y:
#         if maze[nx][ny] == 1 and visited[nx][ny] == 0:
#           need_visited.append({'x': nx, 'y': ny, 'd': cd+1})
#           # print(need_visited)

# bfs(N-1, M-1)
# print(need_visited[0]['d'])