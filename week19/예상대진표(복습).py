def solution(n, a, b):
    answer = 1
    while (a - 1) // 2 != (b - 1) // 2:
        a = (a - 1) // 2 + 1
        b = (b - 1) // 2 + 1
        answer += 1

    return answer