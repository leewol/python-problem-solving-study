from collections import deque

# 올바른 괄호 문자열 판단
def isGoodParen(q):
    stack = []
    
    for p in q:
        if stack and ((stack[-1] == "[" and p == "]") or (stack[-1] == "(" and p == ")") or (stack[-1] == "{" and p == "}")):
            stack.pop()
            continue
            
        stack.append(p)
        
    return False if stack else True

def solution(s):
    answer = 0
    s_q = deque(list(s))
    
    for x in range(len(s_q)):
        s_q.append(s_q.popleft())
        answer = answer + (1 if isGoodParen(s_q) else 0)
    
    return answer