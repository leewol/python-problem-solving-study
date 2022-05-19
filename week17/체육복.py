def solution(n, lost, reserve):
    # 도난 but 여분 있는 학생 제외
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    answer = n - len(new_lost)
    
    # 오름차순 우선순위 : 낮은 번호 > 높은 번호
    for num in sorted(new_lost):
        if (num - 1) in new_reserve:
            new_reserve.remove(num - 1)
        elif (num + 1) in new_reserve:
            new_reserve.remove(num + 1)
        else:
            continue
        answer += 1
        
    return answer