from collections import deque

def solution(priorities, location):
    answer = 0
    prior_q = deque()

    # 인덱스 구별 위해서 만들어준 deque
    # 가장 큰 prior 알기 위해서 (max 함수) prior을 0번째 인덱스로 
    for idx, prior in enumerate(priorities):
        prior_q.append((prior, idx))

    while True:
        max_p = max(prior_q)
        printed = prior_q.popleft()
        
        # 가장 높은 중요도 가진 경우 출력, 아니면 다시 프린트 큐로
        if printed[0] == max_p[0]:   
            answer += 1
            
            # 탈출 조건 : 요청한 문서의 인덱스와 일치
            if printed[1] == location:
                break
                
            continue
            
        prior_q.append(printed)
        
    return answer