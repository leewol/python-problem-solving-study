def solution(absolutes, signs):
  #  for idx, num in enumerate(absolutes):
  #      absolutes[idx] = num if signs[idx] else (-1) * num
  #  return sum(absolutes)
   
    return sum(num if sign else -num for num, sign in zip(absolutes, signs))