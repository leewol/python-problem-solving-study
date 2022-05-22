# 제곱근의 약수의 개수는 항상 홀수 개
# 아니라면 짝수 개
def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        if int(num ** 0.5) == num ** 0.5:
            answer -= num
        else:
            answer += num
            
    return answer


# 일반 for문 풀이
def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        count = 1
        for i in range(1, num):
            count += 1 if num % i == 0 else 0
        
        answer += num if count % 2 == 0 else (-num)
    
    return answer