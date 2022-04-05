### 1541 잃어버린 괄호
# nums = [eval(ex[i]) for i in range(len(ex))] 에러 발생!
ex = input().split('-')
nums = []

for i in range(len(ex)):
  sub_nums = list(map(int, ex[i].split('+')))
  nums.append(sum(sub_nums))

sum = nums.pop(0)

for num in nums:
   sum -= num

print(sum)