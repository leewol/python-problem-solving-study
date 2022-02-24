def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']] # 4*3 키패드 배열
    key_dic = {}
    right_finger = '*'
    left_finger = '#'
    
    for key in numbers:
        if key == 1 or key == 4 or key == 7:
            answer += 'L'
            left_finger = key
        elif key == 3 or key == 6 or key == 9:
            answer += 'R'
            right_finger = key
        else: # 현재 엄지손가락의 위치에 따라 L/R이 정해진다
            for i in range(4):
                for j in range(3):
                    # 연속 같은 키 누를 수도 있지만, 오른손과 왼손의 위치는 같을 수 없다
                    if keypad[i][j] == key:
                        key_dic['key'] = [i, j]
                        
                    if keypad[i][j] == right_finger:
                        key_dic['right_finger'] = [i, j]
                    elif keypad[i][j] == left_finger:
                        key_dic['left_finger'] = [i, j]
                        
            # print(key_dic)
            right_d = abs(key_dic['key'][0] - key_dic['right_finger'][0]) + abs(key_dic['key'][1] - key_dic['right_finger'][1])
            left_d = abs(key_dic['key'][0] - key_dic['left_finger'][0]) + abs(key_dic['key'][1] - key_dic['left_finger'][1])
            if left_d < right_d:
                answer += 'L'
                left_finger = key
            elif right_d < left_d:
                answer += 'R'
                right_finger = key
            else:
                answer += hand[0].upper() 
                if hand == 'left':
                    left_finger = key
                else:
                    right_finger = key
                
    return answer