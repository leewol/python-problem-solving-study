def solution(n):
    answer = 0
    changed = ""
    while n > 0:
        changed = str(n % 3) + changed
        n //= 3
    
    for i, num in enumerate(changed):
        answer += int(num) * (3 ** i)
    
    return answer