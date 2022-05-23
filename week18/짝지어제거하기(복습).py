def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
            continue
        stack.append(char)
    
    return 0 if stack else 1