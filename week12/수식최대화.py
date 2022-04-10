from itertools import permutations
from collections import deque

def solution(expression):
    operator = []
    exp_list = []
    result = []
    
    # 1. 연산 문자열을 배열로 변환
    idx = 0
    while not expression.isdigit():
        char = expression[idx]
        
        if not char.isdigit():
            # 연산자 배열 따로 담기
            if char not in operator:
                operator.append(char)
            
            # 숫자, 연산자 저장
            exp_list.append(expression[:idx])
            exp_list.append(char)
            expression = expression[idx+1:]
            idx = 0
            continue
            
        idx += 1
    
    exp_list.append(expression)

    # 2. 가능한 조합 모두 계산해 본 뒤 저장
    for p in permutations(operator, len(operator)):       
        copy_exp_list = deque(exp_list)
        # 연산자 하나하나에 접근
        for op in p:
            cal_list = []
            while copy_exp_list:
                exp = copy_exp_list.popleft()
                
                if exp == op:
                    if op == "+":
                        num = int(cal_list.pop()) + int(copy_exp_list.popleft())
                    elif op == "-":
                        num = int(cal_list.pop()) - int(copy_exp_list.popleft())
                    elif op == "*":
                        num = int(cal_list.pop()) * int(copy_exp_list.popleft())
                        
                    cal_list.append(str(num))
                    continue
                
                cal_list.append(exp)
            
            copy_exp_list = deque(cal_list.copy())
            
        result.append(abs(int(cal_list[0])))
    
    return max(result)