### 15829 Hashing --- 아스키코드: a(97) ~ z(122) 
L = int(input()) # 문자열 길이
string = input() # 영문 소문자로만 구성된 문자열
hash_num = 0

for i in range(L):
  hash_num += (ord(string[i])-96) * (31 ** i)

print(hash_num % 1234567891)

# math.pow 결과와의 차이 ?