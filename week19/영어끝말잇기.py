def solution(n, words):
    stack = []
    for idx, word in enumerate(words):
        if idx > 0:
            if words[idx-1][-1] != word[0] or word in stack:
                return [(idx % n) + 1, (idx // n) + 1]
        stack.append(word)
        
    return [0, 0]