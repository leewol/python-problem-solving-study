def solution(numbers):
    numbers = sorted(numbers, key=lambda n: str(n) * 3, reverse=True)
    return str(int("".join(map(str, numbers))))