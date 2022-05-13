from math import ceil

def solution(fees, records):
    answer = []
    rec_dic = {}
    full_time = []
    basic_time, basic_fee = fees[0], fees[1]
    per_time, per_fee = fees[2], fees[3]
    
    # 기록 딕셔너리로 만들기
    for rec in records:
        time, nums, memo = rec.split()
        
        if nums not in rec_dic:
            rec_dic[nums] = []
            
        hours, mins = map(int, time.split(":"))
        rec_dic[nums].append((hours, mins))
    
    # 차량 번호 오름차순 정렬
    rec_sorted = sorted(rec_dic.items())
    
    # 누적 시간 및 요금 계산
    for rec in rec_sorted:
        full_time = 0
        for idx, time in enumerate(rec[1]):
            # 짝수번째 => 앞 값 이용해서 계산
            if idx % 2 == 1:
                full_time += (time[0] - rec[1][idx-1][0]) * 60 + (time[1] - rec[1][idx-1][1])
                continue
            # 홀수번째 => 마지막 원소면 23:59 기준 계산
            if idx+1 == len(rec[1]):
                full_time += (23 - time[0]) * 60 + (59 - time[1])
        
        # 기본 시간 초과 시 (기본 요금 + 추가 요금) 아니면 (기본 요금)
        if full_time > basic_time:
            final_fee = basic_fee + ceil((full_time - basic_time) / per_time) * per_fee
            answer.append(final_fee)
        else:
            answer.append(basic_fee)
    
    return answer