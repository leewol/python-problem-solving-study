### 2292 벌집
num = int(input())

honeycomb = 1
count = 1

while num > honeycomb:
  honeycomb += 6 * count
  count += 1

print(count)