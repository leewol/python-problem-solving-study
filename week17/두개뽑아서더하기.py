from itertools import combinations

def solution(numbers):
    combs = combinations(numbers, 2)
    return sorted(set([sum(comb) for comb in list(combs)]))