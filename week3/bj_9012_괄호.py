### 9012 괄호
n = int(input())

for _ in range(n):
  ps = input()
  stack = []
  check = True

  for p in ps:
    if p == '(':
      stack.append(p)
    elif p == ')':
      if not stack:
        check = False
        break
      else:
        stack.pop()
  
  if check == True and not stack:
    print('YES')
  else:
    print('NO')