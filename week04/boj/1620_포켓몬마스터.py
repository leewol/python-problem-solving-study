### 1620 나는야 포켓몬 마스터 이다솜
import re
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poke_dic_id = {}
poke_dic_name = {}

for i in range(1, N+1):
  pokemon = input().strip('\n')
  poke_dic_id[i] = pokemon
  poke_dic_name[pokemon] = i

for _ in range(M):
  q = input().strip('\n')

  if re.match('\d', q) == None: # 문자열
    print(poke_dic_name[q])
  else: # 숫자
    print(poke_dic_id[int(q)])
