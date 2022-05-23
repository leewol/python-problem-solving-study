from collections import deque

def solution(numbers, target):
    answer = 0
    need_visited = deque([(numbers[0], 0), (-numbers[0], 0)])

    while need_visited:
        num, idx = need_visited.popleft()
        idx += 1
        
        if idx < len(numbers):
            need_visited.append((num + numbers[idx], idx))
            need_visited.append((num - numbers[idx], idx))
        else:
            if num == target:
                answer += 1
        
    return answer