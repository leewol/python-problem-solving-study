import re

def solution(new_id):   
    f_id = re.sub('[^a-z0-9-_.]', '', new_id.lower()) # 1, 2
    s_id = re.sub('[.]{2,}', '.', f_id) # 3
    t_id = re.sub('^\.|\.$', '', s_id) # 4
    f_id = re.sub('^$', 'a', t_id) # 5
    answer = re.sub('\.$', '', f_id[0:15]) # 6
    length = len(answer)
    
    return answer + answer[-1]*(3-length) if length < 3 else answer