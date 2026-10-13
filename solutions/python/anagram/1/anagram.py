from typing import Counter
def find_anagrams(word:str, candidates:list[str]):
    if len(candidates) == 1:
        return []
    word = word.lower()
    word_counter = Counter(word)
    result = []
    for target in candidates:
        if target.lower() == word:
            continue
        if Counter(target.lower()) == word_counter:
            result.append(target)
    return result