# 2차 답안
# 비트 연산자, bin(), zip()
def solution(n, arr1, arr2):
    treasure = []
    
    for vals in zip(arr1, arr2):
        row = bin(vals[0]|vals[1])[2:] 
        row = row.replace("1", "#").replace("0", " ")
        row = " " * (n-len(row)) + row
        
        treasure.append(row)
        
    return treasure

# 1차 답안
#     def map_change(arr):
#         map = []
#         for num in arr:
#             bin_nums = [" " for _ in range(n)]

#             for i in range(n):
#                 if num % 2:
#                     bin_nums[-(i+1)] = "#"
#                 else:
#                     bin_nums[-(i+1)] = " "

#                 num = num // 2

#             map.append("".join(bin_nums))

#         return map
    
#     map1 = map_change(arr1)
#     map2 = map_change(arr2)
    
#     for i in range(n):
#         row = ''
#         for j in range(n):
#             if map1[i][j] == map2[i][j] == " ":
#                 row += " "
#             elif map1[i][j] == "#" or map2[i][j] == "#":
#                 row += "#"
                
#         treasure.append(row)
    
#        return treasure