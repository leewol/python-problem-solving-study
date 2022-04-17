from collections import deque              
    
def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = len(maps), len(maps[0])
    visited = [([0] * m) for _ in range(n)]
    
    need_visited = deque()
    need_visited.append((0, 0))
    visited[0][0] = 1
    
    while need_visited:
        cx, cy = need_visited.popleft()

        # 어차피 끝까지 보게 돼있음
        # if cx == n - 1 and cy == m - 1:
        #     break

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 0 and visited[nx][ny] == 0:
                need_visited.append((nx, ny))
                visited[nx][ny] = 1 # 더 빨리 걸러지도록
                maps[nx][ny] = maps[cx][cy] + 1
        
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]