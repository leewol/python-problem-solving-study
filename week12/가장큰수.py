def solution(numbers):
    numbers = list(map(str, numbers))   
  
    # 오름차순 정렬
    # number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    numbers.sort(key=lambda num: num * 3, reverse=True)

    return str(int(''.join(numbers))) # 0 여러 개 처리