### 1085 직사각형에서 탈출 
x, y, w, h = map(int, input().split())
lengths = [x, y, w-x, h-y]

print(min(lengths))
