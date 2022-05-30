# 짝수의 경우 마지막 bit를 0 -> 1로 바꾸면 해결
# 홀수는 두 가지로 나뉨 -> 2진수로 변환했을 경우 모든 비트가 1(ex. 7 : 111), 모든 비트가 1이 아닌 경우(ex. 9 : 1001)
# 제일 마지막에 나오는 0을 1로 바꾸고, (마지막 나오는 0 위치 + 1) 인덱스를 0으로 바꾸면 해결
def solution(numbers):
    answer = []
    
    for number in numbers:
        bits = list("0" + bin(number)[2:])
        idx = "".join(bits).rfind('0')
        bits[idx] = "1"
        
        if number % 2:
            bits[idx + 1] = '0'
        answer.append(int(''.join(bits), 2))
        
    return answer