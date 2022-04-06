def solution(s):
    stack = []
    
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
            continue
        
        stack.append(c)
    
    if stack:
        return 0
    
    return 1