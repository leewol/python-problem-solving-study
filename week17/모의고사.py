def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = {1: 0, 2: 0, 3: 0}
    answer = []
    
    for idx, ans in enumerate(answers):
        if one[idx % len(one)] == ans:
            scores[1] += 1
        if two[idx % len(two)] == ans:
            scores[2] += 1
        if three[idx % len(three)] == ans:
            scores[3] += 1

    for num, score in scores.items():
        if score == max(scores.values()):
            answer.append(num)
    
    return answer