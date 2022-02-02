### 2231 분해합
num = int(input())

for i in range(1, num+1):
  decompose = i + sum((map(int, str(i)))) # i의 분해합
  # i가 작은 수부터 차례로 들어가므로 
  # 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
  if decompose == num:
    print(i)
    break
  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
  if i == num:
    print(0)