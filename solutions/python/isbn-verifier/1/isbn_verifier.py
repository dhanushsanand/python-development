def is_valid(isbn:str):
    isbn = isbn.replace("-", "")
    list_isbn = list(isbn)
    for index, ch in enumerate(list_isbn):
        if ch.isalpha() and ch != 'X':
            return False
        if ch == 'X':
            if index != 9:
                return False
            list_isbn[index] = 10
        else:
            list_isbn[index] = int(ch)
    if len(list_isbn) != 10:
        return False
    multiplier = 10
    sum_isbn, i = 0, 0
    while multiplier > 0:
        sum_isbn += int(list_isbn[i]) * multiplier
        multiplier -= 1
        i += 1
    return sum_isbn % 11 == 0 
