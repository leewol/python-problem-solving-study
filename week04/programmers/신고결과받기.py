def solution(id_list, report, k):
    # 딕셔너리, 변수 초기화
    reporter, reportee, answer_list = {}, {}, {}
    answer = []

    for i in id_list:
        reporter[i] = {}
        answer_list[i] = 0
    
    # 신고 처리
    for rep in report:
        do_id, get_id = rep.split()
        
        # reporter
        if do_id not in reporter: # 이전에 처리한 적 없는 신고자 reporter에 넣기
            reporter[do_id] = {get_id: 1}
        elif get_id not in reporter[do_id]: # 처음 신고받는 사람 넣기
            reporter[do_id][get_id] = 1   
        else:               # 같은 사람을 이전에 신고당한 적 있다면 횟수 증가
            reporter[do_id][get_id] += 1 
            
        # reportee
        if get_id not in reportee : # 첫 번째 신고 reportee에 넣기
            reportee[get_id] = 1
        elif reporter[do_id][get_id] == 1: # 신고자 상관없이 첫 번째로 받는 신고가 아니지만, reporter에 1번 등록되었을 때 이 경우 한 번만 + 해줌
             reportee[get_id] += 1
    
    # 정지 처리
    for i in reportee.items():
        if i[1] >= k:
            stop_id = i[0] # 정지 대상
            
            for r in reporter.items():
                if stop_id in r[1]:
                    answer_list[r[0]] += 1
                    
    for val in answer_list.values():
        answer.append(val)
    
    return answer