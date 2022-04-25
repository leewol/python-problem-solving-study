# 아스키코드 A:65 ~ Z:90 (0~25)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1. A에서 다음/이전 중 어디로 가는 게 더 빠른지 판단해야 함
# 2. 이름에 A가 포함되면, A인 알파벳은 건드리지 않고 완성할 수 있도록 해야 함

def countAlpha(alpha):
    # N이 중간 알파벳, 같거나 작으면 위로
    # 이후에 있는 경로는 아래로
    if alpha <= "N": 
        count = ord(alpha) - 65
    else:
        count = abs(ord(alpha) - 91)
        
    return count
    
def solution(name):
    count = 0
    min_move = len(name) - 1 # 기본 최소 횟수
    
    for idx, alpha in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        count += countAlpha(alpha)
        
        # 해당 알파벳 이후 연속되는 A 찾기
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        
        # 기존, 연속된 A의 왼쪽 시작 방식, 연속된 A의 오른쪽 시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * idx + len(name) - next_idx, idx + 2 * (len(name) - next_idx)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가   
    count += min_move
    
    return count