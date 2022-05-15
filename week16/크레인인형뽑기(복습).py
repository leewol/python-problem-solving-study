# 가장 중요한 것 : 한 번 뺐으면 반복문 빠져나오기
def solution(board, moves):
    answer = 0
    bucket = []
    
    # 해당하는 col의, 0이 아닌 가장 위의 숫자를 추출
    # 0이 아닌 경우, bucket에 담지만 2개 연속이면 터트림
    for col in moves:
        for row in range(len(board)):
            num = board[row][col-1]
            if num != 0:
                board[row][col-1] = 0
                if bucket and bucket[-1] == num:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(num)
                break
                
    return answer