def solution(lottos, win_nums):
    count = 0
    zero_count = 0
    prize = [6, 6, 5, 4, 3, 2, 1]
    # prize = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    for i in lottos:
        # 당첨번호에 존재하는 경우
        if i in win_nums:
            count += 1
        elif i == 0:
            zero_count += 1
    
    return prize[count+zero_count], prize[count]