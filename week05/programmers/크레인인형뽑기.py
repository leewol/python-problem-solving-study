def solution(board, moves):
    bucket = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            check = board[i][move-1]
            
            if check != 0:
                bucket.append(check)
                board[i][move-1] = 0
                break # 한 번 빼면 끝
        
        length = len(bucket)
        
        if length > 1 and bucket[-1] == bucket[len(bucket)-2]:
            bucket.pop()
            bucket.pop()
            answer += 2
    
    return answer