# 비트 연산, bin(), replace(), zip(), zfill()
def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        row = bin(num1|num2)[2:].zfill(n)
        row = row.replace("1", "#").replace("0", " ")
        answer.append(row)
        
    return answer