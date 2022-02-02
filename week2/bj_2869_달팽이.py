## 2869 달팽이는 올라가고 싶다
go, down, V = map(int, input().split())
now = V - go
count = 1
move = go - down

if now % move == 0:
  count += now // move
else:
  count += (now // move) + 1

print(count)