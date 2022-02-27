### 1992 쿼드트리
import sys

input = sys.stdin.readline
N = int(input()) # 2의 제곱수, 1(2^0) <= N <= 64(2^6)
video = []
zip = ''

def cut(x, y, n):
  global zip
  check = video[x][y]
    
  for i in range(n):
    for j in range(n):
      if video[x+i][y+j] != check:
        zip += '('
        cut(x, y, n//2)
        cut(x, y + n//2, n//2)
        cut(x + n//2, y, n//2)
        cut(x + n//2, y + n//2, n//2)
        zip += ')'
        return
        
  zip += check
  
for _ in range(N):
  row = list(input().rstrip())
  video.append(row)

if N == 1:
    print(f'({video[0][0]})')
else:
  cut(0, 0, N)
  print(zip)