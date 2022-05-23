from collections import deque

def solution(numbers, target):
    answer = 0
    need_visited = deque()
    n = len(numbers)

    need_visited.append([numbers[0], 0])
    need_visited.append([-1 * numbers[0], 0])
    
    while need_visited:
        val, idx = need_visited.popleft()
        idx += 1
        
        if idx < n:
            need_visited.append([val + numbers[idx], idx])
            need_visited.append([val - numbers[idx], idx])
        else:
            if val == target:
                answer += 1
    
    return answer