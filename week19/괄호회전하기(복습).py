# 올바른 괄호 검사 함수
def isCorrect(s):
    stack = []
    for char in s:
        if stack and ((char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "[") or (char == "}" and stack[-1] == "{")):
            stack.pop()
            continue
        stack.append(char)

    return True if not stack else False
    
def solution(s):   
    # 회전하면서 총 몇 번 올바른 괄호가 나타나는지 계산
    count = 0
    
    for x in range(len(s)):
        count += 1 if isCorrect(s) else 0
        s = s[1:] + s[0]
    
    return count