### 11723 집합
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시
# check x: S에 x가 있으면 1을, 없으면 0을 출력 (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가 (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로
# empty: S를 공집합으로 

from collections import deque
import sys
input = sys.stdin.readline

M = int(input())
S = deque([])

for _ in range(M):
  request = input().split()

  req = request[0]
  if len(request) == 2:
    num = int(request[1])

  if req == 'add':
    if num not in S:
      S.append(num)
  elif req == 'remove':
    if num in S:
      S.remove(num)
  elif req == 'check':
    if num in S:
      print(1)
    else:
      print(0)
  elif req == 'toggle':
    if num in S:
      S.remove(num)
    else:
      S.append(num)
  elif req == 'all':
    S = deque([x for x in range(1, 21)])
  elif req == 'empty':
    S = deque([])