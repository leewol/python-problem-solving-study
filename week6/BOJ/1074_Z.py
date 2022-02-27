### 1074 Z
N, r, c = map(int, input().split())

# 분할정복
count = 0

while N != 0:
  N -= 1
  
  if r < 2**N and c < 2**N: # 1
    count += (2 ** N) * (2 ** N) * 0
  elif r < 2**N and c >= 2**N: # 2
    count += (2 ** N) * (2 ** N) * 1
    c -= ( 2 ** N )
  elif r >= 2**N and c < 2**N: # 3
    count += (2 ** N) * (2 ** N) * 2
    r -= ( 2 ** N )
  else: # 4
    count += (2 ** N) * (2 ** N) * 3
    c -= ( 2 ** N )
    r -= ( 2 ** N )

print(count)

# 재귀함수 - 시간 초과 

# n = 2 ** N
# arr = [[0 for _ in range(n)] for _ in range(n)]
# count = 0

# def visitZ(x, y, n):
#   global count

#   if n == 2:
#     for i in range(n):
#       for j in range(n):
#         arr[x+i][y+j] = count
#         count += 1
#   else:
#     visitZ(x, y, n // 2)
#     visitZ(x, y + n // 2, n // 2)
#     visitZ(x + n // 2, y, n // 2)
#     visitZ(x + n // 2, y + n // 2, n // 2)

# visitZ(0, 0, n)
# print(arr[r][c])