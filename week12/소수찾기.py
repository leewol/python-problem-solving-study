from itertools import permutations

def solution(numbers):
    num_list = []
    count = 0
    
    # 주어진 숫자 종이 조각으로 만들 수 있는 숫자
    for num in numbers:
        if int(num) not in num_list:
            num_list.append(int(num))
    
    for i in range(2, len(numbers) + 1):
        perms = list(set(permutations(list(numbers), i)))
        
        for p in perms:
            p_num = int("".join(p))
            if p_num not in num_list:
                num_list.append(p_num)
    
    # 소수인지 아닌지 판단하여 개수 세기 - 에라토스테네스의 체
    max_n = max(num_list)
    sieve = [1] * (max_n + 1)
    sieve[0], sieve[1] = 0, 0
    
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i+i, max_n + 1, i):
                sieve[j] = 0
    
    for num in num_list:
        if sieve[num] == 1:
            count += 1
            
    return count