def solution(arr1, arr2):
    c, r, r2 = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [([0] * r2) for _ in range(c)]
    
    for n in range(r2):
        for i in range(c):
            num = 0
            for j in range(r):
                num += arr1[i][j] * arr2[j][n]
            answer[i][n] = num
            
    return answer