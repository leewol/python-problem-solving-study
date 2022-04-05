### 1920 수 찾기
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

# 기본적인 방법.. (순차 탐색)
# for num in M_list:
#   if num in N_list:
#     print(1)
#   else:
#     print(0)

# 시간 제한 맞추기 위해서는? -> Binary Search 이용
N_list.sort() # 오름차순 정렬

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2

  if array[mid] == target: # 원하는 값 찾은 경우
    return mid
  elif array[mid] > target: # 원하는 값이 중간점 값보다 작은 경우 왼쪽 확인
    return binary_search(array, target, start, mid - 1)
  else: # 원하는 값이 중간점 값보다 큰 경우 오른쪽 확인
    return binary_search(array, target, mid + 1, end)

for num in M_list:
  result = binary_search(N_list, num, 0, N - 1)
  if result is None:
    print(0)
  else:
    print(1)