### 11651 좌표 정렬하기 2
n = int(input())
coordinates = []

for _ in range(n):
  x, y = map(int, input().split())
  coordinates.append((x, y))

new_coor = sorted(coordinates, key=lambda x: (x[1], x[0]))

for i in new_coor:
  print(f'{i[0]} {i[1]}')
