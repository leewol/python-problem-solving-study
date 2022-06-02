# BFS 이용하여 최단거리 구하기
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [([0] * m) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    need_visited = deque([(0, 0)])
    visited[0][0] = 1
    
    while need_visited:
        cx, cy = need_visited.popleft()
        
        for move in range(4):
            nx, ny = cx + dx[move], cy + dy[move]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                need_visited.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
    
    return -1 if visited[n-1][m-1] == 0 else visited[n-1][m-1]