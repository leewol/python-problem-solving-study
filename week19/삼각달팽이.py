def solution(n):
    temp_list = [[0 for j in range(i+1)] for i in range(n)]
    num = 1
    i, j = -1, 0
    # 밑 방향 -> 0 , 오른쪽 -> 1, 위쪽 -> 2
    for dir in range(n): 
        for corr in range(dir, n):
            if dir % 3 == 0:
                i += 1
            elif dir % 3 == 1:
                j += 1
            else:
                i -= 1
                j -= 1
            temp_list[i][j] = num
            num += 1
    
    return sum(temp_list, [])