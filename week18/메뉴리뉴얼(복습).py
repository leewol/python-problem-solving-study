from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    course_combs = []
    
    for order in orders:
        for num in course:
            course_combs.extend(combinations(order, num))
    
    for idx, comb in enumerate(course_combs):
        course_combs[idx] = "".join(sorted(comb))
        
    
    for num in course:
        course_dic = sorted(filter(lambda x:x[1] >= 2 and len(x[0]) == num, Counter(course_combs).items()), key=lambda x:(-x[1], x[0]))
        
        if not course_dic:
            break
            
        max_cnt = course_dic[0][1]
        
        for c in course_dic:
            if c[1] < max_cnt:
                break
            answer.append(c[0])
            
    return sorted(answer)