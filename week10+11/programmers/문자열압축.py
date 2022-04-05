def solution(s):
    l = len(s)
    min_len = l + 1
    
    if l == 1:
        return l
    
    for i in range(1, l // 2 + 1): # 기준 str 길이 변경
        answer_str = ""
        count = 1
        cmp_str = s[:i] # 기준 
        
        for j in range(i, l + 1, i): # 주어진 str 검사           
            if cmp_str == s[j:j+i]:
                count += 1
                continue
            
            answer_str += str(count) + cmp_str if count > 1 else cmp_str
            cmp_str = s[j:j+i]
            count = 1
        
        # 기준 str 길이가 l에 딱 맞지 않아서 남아 버린 나머지 str 처리
        # ex) "aabbaccc"를 3씩 자르면 "aab/bac/cc"가 되고, 총 길이 8보다 9가 큼
        # 그래서 for문 마지막에 cmp_str = "cc"가 남은 채로 answer_str = "aabbac"로 끝남
        # 따라서 넣어 주지 못한 cmp_str을 넣어 주어야 한다
        answer_str += str(count) + cmp_str if count > 1 else cmp_str
        
        min_len = min(min_len, len(answer_str))
    
    return min_len
