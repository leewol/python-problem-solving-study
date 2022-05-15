def solution(s):
    s_len = len(s)
    s_min = 1000
    
    for i in range(1, s_len // 2 + 1): # 압축 단위
        j = 0
        count = 1
        s_zip = ""
        
        while j < s_len: # 문자열 돌기
            if s[j:j+i] == s[j+i:j+2*i]:
                count += 1
            else:
                if count > 1:
                    s_zip += str(count) + s[j:j+i]
                    count = 1
                elif count == 1:
                    s_zip += s[j:j+i]
            j = j + i
            
        # min 업데이트
        if s_min > len(s_zip):
            s_min = len(s_zip)
            
    return s_min if s_len > 1 else s_len 