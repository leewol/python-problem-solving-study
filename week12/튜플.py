def solution(s):
    set_list = []
    result = []
    
    # 문자열 자료를 리스트로 변경
    s = s.split('}')
    
    for tup in s:
        tup_set = list(map(int, filter(None, tup.replace('{', '').split(','))))
        
        if tup_set:
            set_list.append(tup_set)
    
    # 길이가 짧은 배열부터 보기 위해 정렬
    set_list = sorted(set_list, key=lambda x:len(x))
    
    for t_set in set_list:
        for num in t_set:
            if num not in result:
                result.append(num)
    
    return result