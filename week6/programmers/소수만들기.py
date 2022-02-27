import itertools

def solution(nums):
    # 에라토스테네스의 체
    sieve = [True] * 3001
    sieve[0], sieve[1] = False, False
    m = int(3000 ** 0.5)
    
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, 3001, i):
                sieve[j] = False
    
    # 3개의 수 경우의 수, 소수 개수 구하기
    count = 0
    combs = itertools.combinations(nums, 3)
    
    for comb in combs:
        c_sum = sum(comb)
            
        if sieve[c_sum] == True:
            count += 1
    
    return count