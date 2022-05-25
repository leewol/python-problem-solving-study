# 던전 최대 8곳

# 1. 순열 풀이
from itertools import permutations

def solution(k, dungeons):
    max_cnt = 0
    
    for perm in permutations(dungeons, len(dungeons)):
        stam = k
        cnt = 0
        for dungeon in perm:
            if stam < 0:
                break
            if dungeon[0] <= stam:
                stam -= dungeon[1]
                cnt += 1
        max_cnt = max(cnt, max_cnt)
    
    return max_cnt

# 2. DFS + 백트래킹
answer = 0

def dfs(k, cnt, dungeons):
    global answer
    
    if cnt > answer:
        answer = cnt

    for i in range(N):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = 0

def solution(k, dungeons):
    global N, visited
    
    N = len(dungeons)
    visited = [0] * N
    
    dfs(k, 0, dungeons)
    
    return answer