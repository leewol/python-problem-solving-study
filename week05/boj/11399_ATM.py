### 11399 ATM
N = int(input())
times = list(map(int, input().split()))
min_time = 0

sorted_times = sorted(times)

for i in range(N):
  for j in range(i+1):
    min_time += sorted_times[j]

print(min_time)