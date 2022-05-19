from itertools import combinations

def solution(nums):
    count = 0
    
    # 서로 다른 3개 고르기
    combs = list(combinations(nums, 3))
    
    # 그 합이 소수인지 판단
    for comb in combs:
        num = sum(comb)
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1
            
    return count