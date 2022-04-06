# in_out 배열, msg_dic 만들지 않고 메시지 순서대로 출력 다시 풀어 보기! 

def solution(record):
    answer = []
    in_out = []
    user_dic = {}
    msg_dic = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    for r in record:
        r = r.split()
        
        if r[0] == "Enter":
            in_out.append((r[0], r[1]))
            user_dic[r[1]] = r[2]
            
        elif r[0] == "Leave":
            in_out.append((r[0], r[1]))

        elif r[0] == "Change":
            user_dic[r[1]] = r[2]
            
    for rec in in_out:
        msg = user_dic[rec[1]] + msg_dic[rec[0]]
        answer.append(msg)

    return answer