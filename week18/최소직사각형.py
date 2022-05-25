# 작은 것 중에 큰것, 큰 것 중에 큰것
def solution(sizes):
#     sizes = [sorted(size) for size in sizes]
#     max_w, max_h = 0, 0
    
#     for w, h in sizes:
#         max_w = max(w, max_w)
#         max_h = max(h, max_h)
    
#     return max_w * max_h
  
    return max(max(size) for size in sizes) * max(min(size) for size in sizes)