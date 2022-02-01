### 1152 단어의 개수 
#### --- 파이썬에서 trim -> lstrip(왼쪽 공백)/rstrip(오른쪽 공백)/strip(양쪽)
#### split()은 공백이 여러개여도 무조건 1개로 보고 처리,
#### split(' ')은 공백 하나하나를 각각의 공백으로 따로 처리한다.

string = input().strip().split()
print(len(string))