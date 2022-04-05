### 10866 덱

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deq = deque([])

for _ in range(n):
  request = input().split()
  
  if request[0] == 'push_front':
    deq.appendleft(int(request[1]))
  elif request[0] == 'push_back':
    deq.append(int(request[1]))
  elif request[0] == 'pop_front':
    if not deq:
      print(-1)
    else:
      out = deq.popleft()
      print(out)
  elif request[0] == 'pop_back':
    if not deq:
      print(-1)
    else:
      out = deq.pop()
      print(out)
  elif request[0] == 'size':
    print(len(deq))
  elif request[0] == 'empty':
    if not deq:
      print(1)
    else:
      print(0)
  elif request[0] == 'front':
    if not deq:
      print(-1)
    else:
      print(deq[0])
  elif request[0] == 'back':
    if not deq:
      print(-1)
    else:
      print(deq[-1])