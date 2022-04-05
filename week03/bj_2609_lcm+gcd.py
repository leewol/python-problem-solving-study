### 2609 최대공약수와 최소공배수 --- 애초에 b가 최대공약수여서 못 들어가는 경우 처리
a, b = map(int, input().split())
lcm = a * b

# 더 큰 수를 a로 지정
if a < b:
  tmp = a
  a = b
  b = tmp

# 유클리드 호제법
while True:
  if a%b == 0:
    gcd = b # 최대공약수
    break

  remainder = a % b
  a = b
  b = remainder

lcm //= gcd # 최소공배수