### 1780 종이의 개수
import sys

input = sys.stdin.readline

N = int(input())
paper = []
m_one = 0
zero = 0
one = 0

def cut(x, y, n):
  global zero, one, m_one
  first_num = paper[x][y]

  # 해당 종이의 전체가 같은 숫자인지 검사
  for i in range(x, x+n):
    for j in range(y, y+n):
      # 같은 숫자가 나오지 않았다면 자르기 - 좌->우 한 줄씩 확인
      if first_num != paper[i][j]:
        cut(x, y, n//3)
        cut(x + n//3, y, n//3)
        cut(x + 2*(n//3), y, n//3)
        cut(x, y + n//3, n//3)
        cut(x + n//3, y + n//3, n//3)
        cut(x + 2*(n//3), y + n//3, n//3)
        cut(x, y + 2*(n//3), n//3)
        cut(x + n//3, y + 2*(n//3), n//3)
        cut(x + 2*(n//3), y + 2*(n//3), n//3)
        return

  if first_num == '0':
    zero += 1
    return
  elif first_num == '1':
    one += 1
    return
  elif first_num == '-1':
    m_one += 1
    return

for _ in range(N):
  row = input().split()
  paper.append(row)

cut(0, 0, N)

print(m_one)
print(zero)
print(one)
