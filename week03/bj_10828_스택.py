### 10828 스택

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
  request = input().split()
  
  if request[0] == 'push':
    stack.append(int(request[1]))
  elif request[0] == 'pop':
    if not stack:
      print(-1)
    else:
      out = stack.pop()
      print(out)
  elif request[0] == 'size':
    print(len(stack))
  elif request[0] == 'empty':
    if not stack:
      print(1)
    else:
      print(0)
  elif request[0] == 'top':
    if not stack:
      print(-1)
    else:
      print(stack[-1])