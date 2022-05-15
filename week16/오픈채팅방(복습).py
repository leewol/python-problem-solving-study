def solution(record):
    answer = []
    record_list = []
    user_dic = {}
    msg_dic = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    # 유저 정보, 기록 정보 저장
    for rec in record:
        r = rec.split() # Leave인 경우 닉네임이 없음
        do, user_id = r[0], r[1]
        
        if do == "Leave":
            record_list.append((user_id, do))
            continue
        
        # Enter/Change인 경우
        nickname = r[2]
        user_dic[user_id] = nickname
        
        if do == "Enter":
            record_list.append((user_id, do))
    
    # 결과 출력
    for rec in record_list:
        user_id, do = rec[0], rec[1]
        answer.append(f'{user_dic[user_id]}{msg_dic[do]}')
    
    return answer