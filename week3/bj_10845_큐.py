### 10845 큐

import sys
input = sys.stdin.readline

n = int(input())
queue = []
front = 0
rear = 0

for _ in range(n):
  request = input().split() # ['pop']
  
  if request[0] == 'push': #['push', '1']
    queue.append(int(request[1]))
    rear += 1
  elif request[0] == 'pop':
    if front == rear:
      front = 0
      rear = 0
      print(-1)
    else:
      out = queue.pop(0)
      front += 1
      print(out)
  elif request[0] == 'size':
    print(len(queue))
  elif request[0] == 'empty':
    if front == rear:
      print(1)
    else:
      print(0)
  elif request[0] == 'front':
    if front == rear:
      print(-1)
    else:
      print(queue[0])
  elif request[0] == 'back':
    if front == rear:
      print(-1)
    else:
      print(queue[-1])