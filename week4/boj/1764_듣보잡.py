### 1764 듣보잡
import sys
input = sys.stdin.readline

# 듣도 못한 N, 보도 못한 M
N, M = map(int, input().split())
nu_list = {}
count = 0

for _ in range(N):
  name = input().strip('\n')
  
  if name not in nu_list:
    nu_list[name] = False

for _ in range(M):
  name = input().strip('\n')
  
  if name in nu_list:
    nu_list[name] = True
    count += 1

nugu_list = sorted(nu_list.items(), key=lambda x:x[0])

print(count)
for nugu in nugu_list:
  if nugu[1] == True:
    print(nugu[0])