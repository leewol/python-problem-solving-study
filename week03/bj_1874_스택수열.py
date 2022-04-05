### 1874 스택 수열
import sys
input = sys.stdin.readline

n = int(input())
stack = []
cur_n = 0
answer = []
NO = 'NO'

for _ in range(n):
  seq_n = int(input())

  while cur_n < seq_n:
    cur_n += 1
    stack.append(cur_n)
    answer.append('+')
    
  if stack[-1] == seq_n:
    stack.pop()
    answer.append('-')
  else:
    answer.append(NO)
    break
  
if NO in answer:
  print(NO) 
else:
  for c in answer:
    print(c)