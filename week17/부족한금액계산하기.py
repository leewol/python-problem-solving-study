def solution(price, money, count):
    # 등차수열의 합 : (개수) * (첫항 + 끝항) / 2
    answer = count * (price + price * count) // 2 - money
    return answer if answer > 0 else 0