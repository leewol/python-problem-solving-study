def getGCD(a, b):
    # 유클리드 호제법 - 최대공약수 구하기
    while b != 0:
        gcd = a % b
        a, b = b, gcd
    
    return a

def solution(arr):
    while len(arr) > 1:
        a, b = arr.pop(), arr.pop()
        lcm = a * b // getGCD(a, b)
        
        arr.append(lcm)
    
    return arr[0]