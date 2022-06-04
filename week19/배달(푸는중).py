from collections import deque

def solution(N, road, K):
    # 그래프 만들기 + !! 최솟값 처리 !!
    road_dic = {}
    road_list = []
    
    for r in road:
        a, b, time = r
        if a not in road_dic:
            road_dic[a] = []
        if b not in road_dic:
            road_dic[b] = []
        
        road_dic[a].append((b, time))
        road_dic[b].append((a, time))
        
    # 1번에서부터 BFS로 각각 최단거리 계산
    need_visited = deque()
    visited = [[False, 0] for _ in range(N + 1)]
    
    for r in road_dic[1]:
        need_visited.append(r)
        visited[r[0]] = [True, r[1]]
    visited[1] = [True, 0]
    
    while need_visited:
        cur, c_time = need_visited.popleft()
        
        for r in road_dic[cur]:
            to, time = r
            if visited[to][0] == False:
                need_visited.append((to, time))
                visited[to][0] = True
                visited[to][1] = visited[cur][1] + time    

    return len(list(filter(lambda x: x[0] == True and x[1] <= K, visited)))