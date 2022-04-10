def solution(phone_book):
  # 1. 문자열 정렬 + startswith 이용
  # 문자열인 채로 정렬하면 바로 뒤에 있는 것만 비교해 주면 된다!
  # index 접근 대신 zip() 이용 가능
  # 효율성 TEST 4 : 101ms 정도
    pb = sorted(phone_book)
    
    for i in range(len(pb) - 1):
        if pb[i+1].startswith(pb[i]):
            return False
    
    return True
  
  # 2. 해시 풀이 방법
  # 효율성 TEST 4 : 500ms 정도
  answer = True
  phone_dic = {}

  # 딕셔너리 만들기
  for phone in phone_book:
    phone_dic[phone] = 1

  # 처음부터 숫자 하나씩 잘라붙여 딕셔너리에 존재하는지 확인
  # 자기자신은 제외해야 함
  for phone in phone_book:
    temp = ""
    for num in phone:
      temp += num
      if temp in phone_dic and temp != phone:
        answer = False

  return answer

    # 3. 첫 풀이 방법
    # 효율성 실패 -> 모든 경우의 수 다 봐줬기 때문에
    # 길이 순으로 정렬 (짧은 것이 긴 것에 포함되므로)
    # from itertools import combinations

    pb = sorted(phone_book, key=lambda x:len(x))
    pb_combs = combinations(pb, 2)
    
    for comb in pb_combs:
        if comb[1].startswith(comb[0]):
            return False
    
    return True