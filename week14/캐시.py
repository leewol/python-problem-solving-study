from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    time = 0
    
    # cacheSize 0일 때 처리
    if cacheSize == 0:
        return 5 * len(cities)
    
    # 총 실행시간 구하기
    for city in cities:
        city = city.lower() # 대소문자 구분 X 처리
        
        # cache hit
        if city in cache:
            time += 1
            
            if cache[-1] == city:
                continue
            cache.remove(city)
            
        # cache miss
        else:
            time += 5
            
        if len(cache) >= cacheSize:
            cache.popleft()
        cache.append(city)

    return time