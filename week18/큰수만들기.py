# 1. 조합 및 정렬 -> 시간 초과
# 2. (idx+1)과 비교하여 큰 수 선택 -> 실패
# 3. stack 이용하여 앞에서부터 큰 수만 선택하기
def solution(number, k):
    stack = []
    n = len(number) - k
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    return "".join(stack)[:n]