def solution(id_list, report, k):
    report_dic = { user_id: [] for user_id in id_list }
    id_dic = { user_id: 0 for user_id in id_list }
    
    # 신고 기록하기
    for rep in report:
        reporter, reportee = rep.split()
        
        if reporter not in report_dic[reportee]:
            report_dic[reportee].append(reporter)
    
    # 정지할 유저 결정, 각 유저 메일 수 구하기
    for key, val in report_dic.items():
        if len(val) < k:
            continue

        for user_id in val:
            id_dic[user_id] += 1
    
    return list(id_dic.values())