def solution(array, commands):
    # for문 결과를 그대로 list로
    return [sorted(array[command[0]-1:command[1]])[command[2]-1] for command in commands]