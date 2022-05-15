import re

def solution(s):
    num_dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for idx, num in enumerate(num_dic):
        if num in s:
            s = re.sub(num, str(idx), s)

    return int(s)