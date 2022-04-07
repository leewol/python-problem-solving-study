# 모든 주문의 조합(course에 있는) 구한 다음 횟수 딕셔너리 만들기
# 2회 이상인 것 오름차순 정렬
from itertools import combinations

def solution(orders, course):
    answer = []
    course_dic = {}
    
    for order in orders:
        for n in course:
            # 주문마다 만들 수 있는 조합 생성
            order_list = list(combinations(list(order), n))
            
            for comb in order_list:
                comb_str = "".join(sorted(comb)) # XW/WX 같은 것 처리 위해 정렬
                
                # 딕셔너리에 저장
                if comb_str not in course_dic:
                    course_dic[comb_str] = 1
                    continue
                course_dic[comb_str] += 1
    
    course_dic = sorted(course_dic.items(), key=lambda c:-c[1])
    
    # 원하는 갯수마다 코스요리 조합 고르기
    # 오름차순 정렬 했으니까 첫 번째로 나오는 게 가장 큰 수
    for n in course:
        c_dic = list(filter(lambda el: len(el[0]) == n and el[1] >= 2, course_dic))
        
        if c_dic:
            max_cnt = c_dic[0][1]
        
        for menu, cnt in c_dic:
            if cnt == max_cnt:
                answer.append(menu)
    
    # 알파벳 오름차순 정리
    answer.sort()
    
    return answer