import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        min_sco = heapq.heappop(scoville)
        sec_sco = heapq.heappop(scoville)
        
        heapq.heappush(scoville, min_sco + (sec_sco * 2))
        count += 1
    
    return count