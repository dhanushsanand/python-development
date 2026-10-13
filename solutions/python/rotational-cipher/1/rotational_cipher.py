def rotate(text:str, key:int):
    if key == 0 or key == 26:
        return text
    ord_a, ord_A = 97, 65
    text_list = list(text)
    for index, character in enumerate(text_list):
        if character.isalpha():
            if character.isupper():
                ordinal_value = (ord(character) + key - ord_A) % 26
                text_list[index] = chr(ord_A + ordinal_value)
            else:
                ordinal_value = (ord(character) + key - ord_a) % 26
                text_list[index] = chr(ord_a + ordinal_value)
    cipher = "".join(text_list)
    return cipher

# char_repl = (ord('n') + 15- ord('a') ) % 26
# print(rotate("Let's eat, Grandma!", 21))
