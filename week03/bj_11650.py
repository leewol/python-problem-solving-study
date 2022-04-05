## 11650 좌표 정렬하기
n = int(input())
coordinates = []

for _ in range(n):
  x, y = map(int, input().split())
  coordinates.append((x, y))

new_coor = sorted(coordinates, key=lambda x: (x[0], x[1]))

for i in new_coor:
  print(f'{i[0]} {i[1]}')