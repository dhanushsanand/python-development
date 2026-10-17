def sum_of_multiples(limit, multiples):
    list_of_multiples = []
    for number in multiples:
        num = get_multiplier_number(limit, number)
        if num == 0:
            continue
        list_of_multiples.extend([ number * x for x in range(1, num + 1) ])
    return sum(set(list_of_multiples))

def get_multiplier_number(limit, number):
    if number == 0: return 0
    n = (limit // number) if (limit % number != 0) else (limit - number)//number 
    return 0 if n == 0 else n