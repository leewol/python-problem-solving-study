def isgoodparen(p):
    stack = []
    
    for c in p:
        if c == "(":
            stack.append("(")
        elif stack and c == ")":
            stack.pop()
        continue
    
    if stack:
        return False
    
    return True

def makegoodparen(w):
    # 1 : 빈 문자열이면 빈 문자열 반환
    if w == "":
        return ""
    
    # 2 : 2 개의 균형잡힌 괄호 문자열 u, v로 분리
    open_p = []
    close_p = []
    
    for idx, c in enumerate(w):
        if c == "(":
            open_p.append(c)
        elif c == ")":
            close_p.append(c)
        if len(open_p) == len(close_p):
            u = w[:idx+1]
            v = w[idx+1:]
            break
            
    # 3 : u가 올바른 괄호 문자열
    if isgoodparen(u):
        new_p = u + makegoodparen(v)
    
    # 4 : u가 올바른 괄호 문자열이 아님
    else:
        u_list = []
        
        for i, c in enumerate(u):
            if i != 0 and i != len(u) - 1:
                if c == "(":
                    u_list.append(")")
                elif c == ")":
                    u_list.append("(")
                    
        new_p = "(" + makegoodparen(v) + ")" + "".join(u_list)
    
    return new_p
        
    
def solution(p):
    if isgoodparen(p):
        return p
    
    return makegoodparen(p)