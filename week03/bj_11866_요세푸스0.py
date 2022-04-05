### 11866 요세푸스 문제 0 
from collections import deque

# 받은 N만큼 원 초기화 
N, K = map(int, input().split())
circle = deque([i for i in range(1, N+1)])

print('<', end='')
while circle: # cicle에 요소가 존재하지 않으면 break
    for i in range(K-1): # K-1번째까지 ------- .rotate 사용해보기
        circle.append(circle[0]) # 뒤에 해당 요소 추가
        circle.popleft() # 해당 요소 삭제
    print(circle.popleft(), end='') # K번째 요소 삭제, 출력
    if circle:
        print(', ', end='')
print('>')