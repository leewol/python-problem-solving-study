def solution(msg):
    answer = []
    msg_dic = {chr(64 + i): i  for i in range(1, 27)}
    idx = 0
    wc = ""
    
    # 최대 msg의 길이만큼 반복
    while idx < len(msg):
        wc += msg[idx]
        
        # 최대 w 찾기
        if wc in msg_dic:
            idx += 1
            continue
        
        # w+c 사전 등록, w 색인 등록
        msg_dic[wc] = len(msg_dic) + 1
        w = wc[:-1]
        answer.append(msg_dic[w])
        
        wc = ""
    
    # 마지막에 남은 단어 추가
    answer.append(msg_dic[wc])
    
    return answer