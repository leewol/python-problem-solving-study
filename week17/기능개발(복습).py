def solution(progresses, speeds):
    answer = []
    days = 0
    cnt = 1
    
    for progress, speed in zip(progresses, speeds):
        if days != 0:
            # 이미 계산된 날짜가 있고, 먼저 완성된 경우
            if progress + speed * days >= 100:
                cnt += 1
            # 아직 덜 완성된 경우 (다음 배포에 포함)
            else:
                answer.append(cnt)
                progress += speed * days
                days += (100 - progress) // speed if (100 - progress) % speed == 0 else (100 - progress) // speed + 1
                cnt = 1
            continue
        days = (100 - progress) // speed if (100 - progress) % speed == 0 else (100 - progress) // speed + 1
    
    # 마지막에 남은 배포 해 주기
    answer.append(cnt)
    
    return answer