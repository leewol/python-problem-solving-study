def solution(participant, completion):
    race_dic = {}
    answer = ""
    
    for part in participant:
        if part not in race_dic:
            race_dic[part] = 0
        race_dic[part] += 1
        
    for comp in completion:
        race_dic[comp] -= 1
        
    for name, cnt in race_dic.items():
        if cnt:
            answer = name
        
    return answer