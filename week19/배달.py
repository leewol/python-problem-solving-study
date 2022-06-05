### 2. 다익스트라(Dijkstra) 알고리즘 적용
import heapq

def solution(N, road, K):
    INF = int(1e9)
    times = [INF] * (N+1)
    road_dic = {}
    
    # 그래프 만들기
    for r in road:
        a, b, time = r
        if a not in road_dic:
            road_dic[a] = []
        if b not in road_dic:
            road_dic[b] = []
    
        road_dic[a].append([b, time])
        road_dic[b].append([a, time])
    
    # 다익스트라 알고리즘
    def dijkstra(start):
        need_visited = []
        times[start] = 0
        heapq.heappush(need_visited, (start, 0))
        
        while need_visited:
            cur, time = heapq.heappop(need_visited) # 최단거리 노드
            # 이미 방문했거나 최솟값이 아닌 경우
            if times[cur] < time:
                continue
            
            for route in road_dic[cur]:
                cost = time + route[1]
                
                # 현재 정보보다 더 적은 시간이 필요한 경우
                if cost < times[route[0]]:
                    times[route[0]] = cost
                    heapq.heappush(need_visited, (route[0], cost))
    
    dijkstra(1)
    
    return len(list(filter(lambda x: x <= K, times)))
  
### 1. 처음 풀이 : 그냥 BFS 사용 + 여러 경로 중 최솟값 경로 선택
### 보완하려면 하나의 지점의 경로 자체의 최솟값으로 계산되게 구해야 함
### 반타작...
from collections import deque

def solution(N, road, K):
    # 그래프 만들기 + 최솟값 처리
    road_dic = {}
    
    for r in road:
        a, b, time = r
        if a not in road_dic:
            road_dic[a] = []
        if b not in road_dic:
            road_dic[b] = []
        
        # 더 작은 값 선택
        for to in road_dic[a]:
            if b == to[0]:
                to[1] = min(time, to[1])
                break
        else:
            road_dic[a].append([b, time])
            
        for to in road_dic[b]:
            if a == to[0]:
                to[1] = min(time, to[1])
                break
        else:
            road_dic[b].append([a, time])
    
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