### 10814 나이순 정렬
n = int(input())
members = []

for i in range(n):
  age, name = input().split()
  members.append((i, int(age), name))

members.sort(key=lambda member:(member[1], member[0]))

for member in members:
  print(f'{member[1]} {member[2]}')
