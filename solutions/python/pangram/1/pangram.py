from string import ascii_lowercase
def is_pangram(sentence:str):
    new_list = set(sentence.lower())
    pangram = ""
    for char in new_list:
        if char.isalpha():
            pangram += char

    ascii_chars = "".join(sorted(pangram))
    return ascii_chars == ascii_lowercase