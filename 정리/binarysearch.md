# 🔍 Binary Search(이분/이진 탐색)

검색 범위를 계속적으로 절반씩 줄여 나가면서 원하는 값을 찾아가는 알고리즘   

![이진탐색](https://blog.penjee.com/wp-content/uploads/2015/04/binary-and-linear-search-animations.gif)

###### _출처: penjee.com_ 

- 배열 전체의 중간값을 target 값과 비교
- 중간값이 target 값보다 작으면/크면 왼쪽/오른쪽 부분만 선택
- 왼쪽/오른쪽 부분의 중간값을 다시 target과 비교
- 중간값 == target이 될 때까지 실행

<br /> 

## ✔ 특징
- 데이터가 정렬되어 있다면 선형 탐색(linear search)보다 성능이 월등히 좋음
- BigO : `O(log N)`
- 오름차순으로 정렬된 자료 이용
- 구현하는 중 dynamic programming, recursion을 볼 수 있음
  
## ✔ 참고
[Binary Search(이진 탐색) - 파이썬](https://velog.io/@madfinger/Binary-Search%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC)   
[이진탐색(Binary Search) 알고리즘](https://wayhome25.github.io/cs/2017/04/15/cs-16/)   
[잔재미코딩 - 이진탐색](https://www.fun-coding.org/Chapter16-binarysearch.html)   
[\[알고리즘\] 이진 검색 - Binary Search (Python, Java)](https://www.daleseo.com/search-binary/)