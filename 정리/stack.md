# 📚 Stack(스택)

![stack](img/stack.png)

데이터를 일시적으로 쌓아 둔 형태의 자료 구조   
`LIFO` 즉, 가장 나중에 들어온 것이 먼저 나감 (== FILO)   
단순하고 빠른 성능을 위해 사용

<br />

파이썬에서는 리스트 또는 연결리스트로 구현    
내장함수가 있는 list로 구현 시, O(1)의 시간복잡도를 가지는 `list.append()`와 `list.pop()`을 사용하면 됨

파이썬 내장모듈에서는 따로 스택 라이브러리가 존재하지 않음   
보통 `deque` 라이브러리를 import 해서 스택 대신 사용

<br />

- pop(): 스택에서 가장 위에 있는 항목을 제거
- push(item): item 하나를 스택의 가장 윗 부분에 추가
- peek(): 스택의 가장 위에 있는 항목을 반환
- isEmpty(): 스택이 비어 있을 때에 true를 반환

<br />

## ✔ 특징

- 장점
  - 구조가 단순해 구현이 쉬움
  - 데이터 저장/읽기 속도가 빠름   

- 단점 (일반적인 스택)
   - 데이터 최대 갯수를 미리 정해야 함
   - 저장 공간 낭비 발생 가능성

  
## ✔ 참고
[\[자료구조\] 스택(Stack)이란](https://gmlwjd9405.github.io/2018/08/03/data-structure-stack.html)   
[\[Python 자료구조\] 스택(Stack)](https://velog.io/@yeseolee/Python-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack)   
[잔재미코딩 - 스택(Stack)](https://www.fun-coding.org/Chapter06-stack.html)