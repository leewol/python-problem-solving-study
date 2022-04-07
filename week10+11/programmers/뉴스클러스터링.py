# 공백, 특수문자, 숫자 포함 X, 대소문자 구분 X, 다중집합 만들기
def tomultiset(s):
    s = s.lower()
    s_set = []
    
    for i in range(len(s) - 1):
        if s[i:i+2].isalpha():
            s_set.append(s[i:i+2])
    
    return s_set
        
def solution(str1, str2):
    str1_set = tomultiset(str1)
    str2_set = tomultiset(str2)
    str_cmp = str1_set.copy() # 체크용 집합 (결과 : A-B)
    str_inter = []
    
    # A, B 모두 공집합인 경우는 1로 정의
    if not str1_set and not str2_set:
        return 1 * 65536
    
    for el in str2_set:
        if el in str_cmp:
            str_inter.append(el)
            str_cmp.remove(el)            
    
    str_uni = str_cmp + str2_set
    
    # jaccard similiarity
    return int(len(str_inter) / len(str_uni) * 65536)