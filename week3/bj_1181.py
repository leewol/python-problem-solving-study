### 1181 단어 정렬
n = int(input())
word_list = []

for _ in range(n):
  word_list.append(input())

new_list = sorted(sorted(set(word_list)), key=len)

for char in new_list:
  print(char)