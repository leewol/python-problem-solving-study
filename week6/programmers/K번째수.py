def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, n = command
        num = sorted(array[i-1:j])[n-1] # 1번째 == 0번째
        
        answer.append(num)
    
    return answer