# 2. 중복조합 이용한 완전탐색
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False
    max_num = 0

    # 1. 중복 조합을 이용해 라이언의 점수를 만든다. 중복 조합에는 맞힌 점수가 들어간다.
    for res in list(combinations_with_replacement(range(0, 11), n)):

        now = [0 for _ in range(11)]
        for r in res:
            now[10 - r] += 1

        ryan = 0
        apeach = 0
      
        # 2. 라이언의 점수와 어피치 점수를 비교
        for i, (l, p) in enumerate(zip(now, info)):
            if l == p == 0:
                continue
            if p >= l:  
                apeach += 10 - i
            elif l > p:
                ryan += 10 - i
              
        # 3. 총 점수를 비교해 라이언이 큰 경우 결과를 업데이트 해준다.
        if ryan > apeach:
            win = True
            if ryan - apeach > max_num:
                max_num = ryan - apeach
                answer = now
    if not win:
        return [-1]
      
    return answer

# 1. 처음에 틀린 답
# 하나의 규칙 루트는 없다... -> 틀림
# 가능한 경우 다 봐야 함!
def solution(n, info):
    answer = [0] * 11
    max_c = [max(info), 1]
    ryan_s = 0
    apeach_s = 0
    
    for idx, count in enumerate(info):
        # 가장 많이 맞힌 횟수는 일단 제외, 어피치 점수로
        if count == max_c[0] and max_c[1] == 1:
            max_c[1] = 0
            apeach_s += (10 - idx)
            continue
        
        # 라이언 횟수, 점수 계산
        cur_c = count + 1
        
        if n - cur_c >= 0:
            n -= cur_c
            answer[idx] = cur_c
            ryan_s += (10 - idx)
            continue
            
        # 어피치 점수 계산
        if count != 0:
            apeach_s += (10 - idx)
    
    # 어피치랑 비기거나 라이언이 지는 경우 처리
    if apeach_s >= ryan_s:
        return [-1]
    
    # 여러 가지인 경우 가장 낮은 점수에 넘기기
    if n > 0:
        min_c = min(answer)
        for i in range(10, -1, -1):
            if answer[i] == min_c:
                answer[i] = n
                break
    
    return answer