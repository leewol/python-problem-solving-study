import re

def solution(s):
    s = re.sub('zero', '0', s) #0
    s = re.sub('one', '1', s) #1
    s = re.sub('two', '2', s) #2
    s = re.sub('three', '3', s) #3
    s = re.sub('four', '4', s) #4
    s = re.sub('five', '5', s) #5
    s = re.sub('six', '6', s) #6
    s = re.sub('seven', '7', s) #7
    s = re.sub('eight', '8', s) #8
    answer = re.sub('nine', '9', s) #9
    
    return int(answer)