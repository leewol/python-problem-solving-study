# (두 번째 풀이) 도달한 플레이어 수에 누적 합 이용 
def solution(N, stages):
    # 스테이지: [클리어 못한 플레이어 수, 도달한 플레이어 수]
    stage_dic = {n: [stages.count(n), 0] for n in range(1, N+1)}
    
    # 가장 마지막 스테이지에 도달한 플레이어 수 구하기
    for stage in stages:
        stage_dic[N][1] += 1 if stage >= N else 0
        
    # 각 스테이지에 도달한 플레이어 수 구하기
    for stage in range(N-1, 0, -1):
        stage_dic[stage][1] = stage_dic[stage+1][1] + stage_dic[stage][0]
    
    sorted_stage = sorted(stage_dic.items(), key=lambda x: -(x[1][0]/x[1][1]) if x[1][1] > 0 else 0)
    
    return [stage[0] for stage in sorted_stage]


# (첫 풀이) 이중 for문 => 시간 초과
def solution(N, stages):
    # 스테이지: (클리어 못한 플레이어 수, 도달한 플레이어 수)
    stage_dic = {n: [0, 0] for n in range(1, N+1)}
    
    for stage in stages:
        for i in range(1, stage+1):
            if i <= N:
                stage_dic[i][1] += 1
                stage_dic[i][0] = (stage_dic[i][0] + 1) if i == stage else stage_dic[i][0]
    
    sorted_stage = sorted(stage_dic.items(), key=lambda x: -(x[1][0]/x[1][1]) if x[1][1] > 0 else 0)

    return [stage[0] for stage in sorted_stage]