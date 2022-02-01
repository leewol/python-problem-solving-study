### 2675 문자열 반복
for i in range(int(input())):
  iteration, string = input().split()

  result_string = ''
  for j in string:
    result_string += int(iteration) * j
  
  print(result_string)