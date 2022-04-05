def solution(a, b):
  answer = 0
  for i in range(len(a)):
    answer += a[i] * b[i]
  return answer

  # 더 느림
  # dot_product = [a[i]*b[i] for i in range(len(a))]
  #   return sum(dot_product)