# 주의할 것: 동명이인이 있을 수 있다
# 완주하지 못한 사람은 한 명!

# from collections import Counter

def solution(participant, completion):
  # Counter 사용보다 더 빠르다!
  part_count = {}
  comp_count = {}
    
  for part in participant:
    if part not in part_count:
      part_count[part] = 1
    else:
      part_count[part] += 1 
      comp_count[part] = 0
      
  for comp in completion:
    comp_count[comp] += 1
            
  for key, value in part_count.items():
    if value != comp_count[key]:
      return key
    
  # part_count = Counter(participant)
  # comp_count = Counter(completion)

  # return (part_count - comp_count).popitem()[0]