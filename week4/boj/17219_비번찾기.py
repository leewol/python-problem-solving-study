### 17219 비밀번호 찾기
import sys

input = sys.stdin.readline

# 저장된 사이트 수, 찾으려는 사이트 수
N, M = map(int, input().split())
pws = {}

for _ in range(N):
  site, pw = input().split()
  pws[site] = pw

for _ in range(M):
  finding = input().strip('\n')

  if finding in pws:
    print(pws[finding])