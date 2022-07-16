from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        words.extend(list(product("AEIOU", repeat=i)))
    
    for idx, word_tuple in enumerate(sorted(words)):
        if "".join(word_tuple) == word:
            return idx + 1