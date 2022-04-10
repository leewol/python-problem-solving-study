def solution(grid):
    dx = [1, -1, 0, 0] # 아래로/위로/오른쪽으로/왼쪽으로
    dy = [0, 0, 1, -1]
    left = [2, 3, 1, 0]
    right = [3, 2, 0, 1]
    # 각 격자에서의 모든 방향을 이동하였는지 판단하는 리스트 case
    cases = [[[0]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    cycles = []
    
    # 각 격자를 모든 방향에서 진입하여 사이클 판단
    for x in range(len(grid)): # 열
        for y in range(len(grid[0])): # 행
            for init_dir in range(4): # 진입 시 처음 바라보는 방향
                # 이미 이동한 적 있는 방향은 새로 판단하지 않음, skip
                if cases[x][y][init_dir] == 1:
                    continue
                    
                count = 0 # 사이클 길이
                nx, ny, cur_dir = x, y, init_dir
                cur_pos = (nx, ny, cur_dir) # cur_pos 초기화
                
                while True:                  
                    # 한 번 거친 지점, 방향 표시
                    cases[nx][ny][cur_dir] = 1
                    count += 1
                    
                    if grid[nx][ny] == "L":
                        cur_dir = left[cur_dir]
                    elif grid[nx][ny] == "R":
                        cur_dir = right[cur_dir]
                    
                    nx = (nx + dx[cur_dir]) % len(grid)
                    ny = (ny + dy[cur_dir]) % len(grid[0])
    
                    cur_pos = (nx, ny, cur_dir)
                    
                    # 이미 지나온 지점을 같은 방향으로 들어온다면 사이클
                    if nx == x and ny == y and cur_dir == init_dir:
                        cycles.append(count)
                        break

    cycles.sort()
    return cycles