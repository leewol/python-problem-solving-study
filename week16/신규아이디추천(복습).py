# re.sub(찾을 패턴, 대체할 문자, 대상 문자열) 이용하면 편하다
# ^ : 처음 / $ : 끝
import re

def solution(new_id):
    new_id = re.sub('[^a-z0-9-_.]', '', new_id.lower()) # 1, 2
    new_id = re.sub('[.]{2,}', '.', new_id) # 3
    new_id = re.sub('^[.]|[.]$', '', new_id) # 4
    new_id = re.sub('^$', 'a', new_id) # 5
    new_id = re.sub('[.]$', '', new_id[:15]) # 6
    length = len(new_id)
    
    return new_id + new_id[-1] * (3 - length) if length < 3 else new_id