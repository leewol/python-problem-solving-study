# 1차 답안
# 중복 코드 많음, string 한 번 훑으면서 변경할 수 있음 -> 최적화하여 재풀이 필수!
def solution(dartResult):
    result_list = []
    i = 0
    
    while i < len(dartResult):
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            result_list.append('10')
            i += 1
        else:
            result_list.append(dartResult[i])
        
        i += 1

    for idx, dart in enumerate(result_list):
        if not dart.isdigit(): # 대문자 알파벳(S, D, T)
            result_list.pop(idx)
            
            if dart == 'S':
                result_list[idx - 1] = int(result_list[idx - 1])
            elif dart == 'D':
                result_list[idx - 1] = int(result_list[idx - 1]) ** 2
            elif dart == 'T':
                result_list[idx - 1] = int(result_list[idx - 1]) ** 3

    
    for idx, dart in enumerate(result_list):
        if dart == '#':
            result_list.pop(idx)
            result_list[idx - 1] = result_list[idx - 1] * (-1)            
    
    for idx, dart in enumerate(result_list):
        if dart == '*':
            result_list.pop(idx)
            result_list[idx - 1] = result_list[idx - 1] * 2
            
            if idx > 1:
                result_list[idx - 2] = result_list[idx - 2] * 2
                
    return sum(result_list)