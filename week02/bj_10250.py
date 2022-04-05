### 10250 ACM 호텔
tests = int(input())

for i in range(tests):
  h, w, n = map(int, input().split())

  if n % h != 0:
    print((n % h)*100 + (n // h + 1))
  elif n % h == 0:
    print(h*100 + (n // h))