from itertools import permutations

def solution(numbers):    
    answer = 0
    nums = []
    
    # 만들 수 있는 숫자 전체 구하기
    for i in range(len(numbers)):
        for perm in permutations(numbers, i+1):
            num = int("".join(perm))
            if num not in nums and num > 1:
                nums.append(num)
                
    # 소수 판별
    for num in nums:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            answer += 1

    return answer