def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == "(" and char == ")":
            stack.pop()
            continue
        stack.append(char)
            
    return True if not stack else False