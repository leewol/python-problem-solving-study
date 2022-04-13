def solution(s):
    num_list = list(map(int, s.split(' ')))
    
    return f'{min(num_list)} {max(num_list)}'