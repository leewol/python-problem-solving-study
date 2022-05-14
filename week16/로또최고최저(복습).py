def solution(lottos, win_nums):
    ranks = { 0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    zeros = 0
    wins = 0
    
    for num in lottos:
        # 로또 번호와 일치
        if num in win_nums:
            wins += 1
        # 알아볼 수 없는 번호(0)
        if num == 0:
            zeros += 1
    
    # 최고 - (일치하는 개수 + 0 개수) / 최저 - (일치하는 개수)
    return [ranks[wins + zeros], ranks[wins]]