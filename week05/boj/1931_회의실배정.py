### 1931 회의실 배정
import sys

input = sys.stdin.readline

N = int(input())
meetings = []
count = 0

for _ in range(N):
  meeting = list(map(int, input().split()))
  meetings.append(meeting)

meetings = sorted(meetings, key=lambda x:(x[1], x[0]))

end_time = 0

for i, j in meetings:
  if i >= end_time:
    end_time = j
    count += 1

print(count)