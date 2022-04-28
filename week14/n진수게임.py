def solution(n, t, m, p):
    answer = ''
    full_num = '00'
    alpha_dic = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }
    
    # (t * m)개만큼 말할 수 있는 숫자 구하기 
    for num in range(1, t * m):
        changed_num = ''
        while num > 0:
            quot, remain = divmod(num, n)
            num = quot
            changed_num += str(remain) if remain not in alpha_dic else alpha_dic[remain]
        
        changed_num = changed_num[::-1]
        full_num += changed_num
    
    # 그중에서 튜브가 말해야 하는 숫자 t개 구하기
    for i in range(t):
        answer += full_num[p + m*i]
    
    return answer