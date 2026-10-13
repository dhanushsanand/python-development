import string
def reverse(text:str):
    char_list = list(text)

    low, high = 0, len(char_list) -1
    while low <= high:
        char_list[low], char_list[high] = char_list[high], char_list[low]
        low += 1
        high -=1
    text = "".join(char_list)
    return text

print(reverse("stressed"))
