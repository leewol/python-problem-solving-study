### 10809 알파벳 찾기 --- 아스키 코드 이용

# find( )
# 찾는 문자가 없는 경우에 -1을 출력한다.
# 문자열을 찾을 수 있는 변수는 문자열만 사용이 가능하다.  리스트, 튜플, 딕셔너리 자료형에서는 find 함수를 사용할 수 없다. 만일 사용하게 되면 AttributeError 에러가 발생한다.

# index( )
# 찾는 문자가 없는 경우에 ValueError 에러가 발생한다.
# 문자열, 리스트, 튜플 자료형에서 사용 가능하고 딕셔너리 자료형에는 사용할 수 없어 AttributeError 에러가 발생한다.

string = input()

for i in range(97, 123):
  print(string.find(chr(i)), end=' ')