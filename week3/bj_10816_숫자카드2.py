### 10816 숫자 카드 2 -- pypy3 제출
from sys import stdin
input = stdin.readline

have_n = int(input())
have_list = map(int, input().split())
target_n = int(input())
target_list = list(map(int, input().split()))

# 들어온 숫자 횟수 dictionary 만들기
have_dic = {}
for num in have_list:
  if num not in have_dic:
    have_dic[num] = 0
  have_dic[num] += 1

have_dic = sorted(have_dic.items(), key=lambda x:x[0])

# print(have_dic[0][0])

# 입력받은 숫자들의 횟수 찾기
def binary_search(array, target, start, end):
  if start > end:
    return 0
  mid = (start + end) // 2

  if array[mid][0] == target: # 원하는 값 찾은 경우
    return array[mid][1] # 인덱스 값 반환
  elif array[mid][0] > target: # 원하는 값이 중간점 값보다 작은 경우 왼쪽 확인
    return binary_search(array, target, start, mid - 1)
  else: # 원하는 값이 중간점 값보다 큰 경우 오른쪽 확인
    return binary_search(array, target, mid + 1, end)

for target in target_list:
  answer = binary_search(have_dic, target, 0, len(have_dic) - 1)
  print(answer, end=' ')