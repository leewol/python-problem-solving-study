def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    left, right = "*", "#"
    
    for num in numbers:
        # 왼쪽, 오른쪽 고정 값
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            left = num
        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            right = num
        # 유동적인 값 (2, 5, 8, 0)
        else:
            # 왼쪽, 오른쪽 각각 거리 구하기
            for i in range(len(keypad)):
                for j in range(len(keypad[0])):
                    if keypad[i][j] == num:
                        num_pos = (i, j)
                    
                    if keypad[i][j] == left:
                        left_pos = (i, j)
                    elif keypad[i][j] == right:
                        right_pos = (i, j)

            left_d = abs(num_pos[0] - left_pos[0]) + abs(num_pos[1] - left_pos[1])
            right_d = abs(num_pos[0] - right_pos[0]) + abs(num_pos[1] - right_pos[1])
                    
            # 거리 짧은 손 선택 / 동일한 경우, hand 조건 반영
            if left_d < right_d:
                answer += "L"
                left = num
            elif right_d < left_d:
                answer += "R"
                right = num
            else:
                if hand == "left":
                    answer += "L"
                    left = num
                elif hand == "right":
                    answer += "R"
                    right = num

    return answer