from itertools import combinations

def solution(relation):
    attribute = len(relation[0])
    rows = len(relation)
    combs = []
    
    # 가능한 속성 조합
    for idx in range(attribute + 1):
        combs.extend(combinations(range(attribute), idx))
    
    # 후보 키 판단
    candidate = []
    
    for comb in combs:
        comb_rel = [tuple([rel[idx] for idx in comb]) for rel in relation]
        
        # 유일성을 만족하는 것들 중 최소성 판단
        if len(set(comb_rel)) == rows:
            for el in candidate:
                # 판단 중인 조합이 이미 후보 키 list에 들어 있는 것을 부분집합으로 가지면 탈락
                if set(el).issubset(set(comb)): 
                    break
            else:
                candidate.append(comb)
    
    return len(candidate)