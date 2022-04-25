def change_base(n, k):
    changed = ''
    
    while n > 0:
        n, mod = divmod(n, k) # 몫, 나머지
        changed += str(mod)
        
    return changed[::-1]

def solution(n, k):
    count = 0
    num_list = list(map(int, filter(lambda x:x != '', change_base(n, k).split('0'))))
    
    for n in num_list:
        if n != 1:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                count += 1

    return count