### 2164 카드2
# Queue : deque와 달리 방향성이 없기 때문에 데이터 추가와 삭제가 하나의 메서드로 처리된다!
# 데이터를 추가 할 때 : put(x) 메서드를 사용
# 데이터 삭제 : get() 메서드 사용

# deque : double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료구조이다.

# popleft() 라는 메서드를 사용하면 list의 pop(0) 메서드와 같은 효과를 가진다!

from collections import deque

N = int(input())
queue = deque()

for i in range(1, N+1):
  queue.append(i)

while len(queue) != 1:
  queue.popleft()
  to_last = queue.popleft()
  queue.append(to_last)

print(queue[0])