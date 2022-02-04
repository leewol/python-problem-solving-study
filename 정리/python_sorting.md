# ⛓ 파이썬 정렬 함수
```Python
<list>.sort([key = <function>], [reverse = True|False])
```
```Python
sorted(<iterable>, [key = <function>], [reverse = True|False])
```   
## ✔ sort() vs. sorted()

||sort()|sorted()|
|------|------|------|
|사용 범위|list|모든 iterable 객체|
|반환|없음|정렬된 새로운 list|
|원본 변형|O|X|

   
- 기본 정렬 기준은 **오름차순**
- reverse 매개 변수 사용 시 내림차순 정렬 가능
  - sort(reverse=True) / sorted(reverse=True)   
    
## ✔ key 매개변수
key 값을 기준으로 정렬, 기본 정렬 기준은 **오름차순**  
  

```python 
sorted(iterable 객체 이름, key=len)
```
위와 같이 사용하면 길이가 짧은 것부터 오름차순으로 정렬됨 

<br/>

### ➰ lambda 함수
key 매개 변수에 비교함수로 전달하여 원하는 기준을 정할 수 있음
```python
# lambda 정렬 예시
arr = [(1, 2), (0, 1), (5, 1), (4, 2), (3, 5)]
print(sorted(arr, key = lambda x : x[0])) # 요소의 0번째 값만 기준으로 정렬
# [(0, 1), (1, 2), (3, 5), (4, 2), (5, 1)]
print(sorted(arr, key = lambda x : -x[0])) # - 붙여서 내림차순 정렬
# [(5, 1), (4, 2), (3, 5), (1, 2), (0, 1)]
```

```python
# 문자열 정렬 예시
a = ['aa', 'az', 'af', 'ad']
print(sorted(a, key = lambda x : x[0]))
# ['aa', 'az', 'af', 'ad']
print(sorted(a, key = lambda x : (x[0], x[1])))
# ['aa', 'ad', 'af', 'az']
```

## ✔ 참고

[\[Python\]정렬 문법 sort() sorted() reverse](https://velog.io/@aonee/Python-%EC%A0%95%EB%A0%AC-sort-sorted-reverse)   
[\[Python\] 파이썬 커스텀 정렬 - sort(), sorted()](https://cotak.tistory.com/8)   
[파이썬 정렬 함수 sort, sorted _ key = lambda, function / reverse= 파라미터 이용 방법 (Python)](https://ooyoung.tistory.com/59)
