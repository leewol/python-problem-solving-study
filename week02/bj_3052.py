### 3052 나머지 ---- 포함 여부: in/not in
remainders = []

for i in range(10):
  num = int(input())
  if num % 42 not in remainders:
    remainders.append(num % 42)

print(len(remainders))