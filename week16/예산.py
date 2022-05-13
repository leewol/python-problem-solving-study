def solution(d, budget):
    answer = 0
    d.sort()
    
    for idx, req in enumerate(d):
        budget -= req
        
        if budget < 0:
            break
        answer += 1
        
    return answer