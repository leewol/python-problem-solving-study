def solution(A,B):
    answer = 0

    # A, B 정렬
    if max(A) > max(B):
        A.sort(reverse=True)
        B.sort()
    else:
        B.sort(reverse=True)
        A.sort()
    
    # 누적 합 구하기
    for a, b in zip(A, B):
        answer += a * b

    return answer