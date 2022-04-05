### 4949 균형잡힌 세상 -- Stack

while True:
  string = input()
  stack = []
  check = True

  if string == '.':
    break

  for char in string:
    if char == '(' or char == '[':
      stack.append(char)
    elif char == ')':
      if not stack or stack[-1] == '[':
        check = False
        break
      elif stack[-1] == '(':
        stack.pop()
    elif char == ']':
      if not stack or stack[-1] == '(':
        check = False
        break
      elif stack[-1] == '[':
        stack.pop()
  
  if check == True and not stack:
    print('yes')
  else:
    print('no')
