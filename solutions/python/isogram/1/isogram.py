def is_isogram(phrase:str):
    phrase_list = list(phrase.lower())
    phrase_without_spaces = ""
    for item in phrase_list:
        if item.isalpha():
            phrase_without_spaces += item
    return True if len(phrase_without_spaces) == len(set(phrase_without_spaces)) else False
