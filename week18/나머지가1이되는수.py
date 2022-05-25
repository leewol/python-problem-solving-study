def solution(n):
    for num in range(2, int((n-1) ** 0.5) + 1):
        if (n - 1) % num == 0:
            return num
    return n - 1