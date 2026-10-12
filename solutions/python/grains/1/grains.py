def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    count = 1
    if number == 1:
        return count
    for _ in range(2, number + 1):
        count = count * 2
    return count


def total():
    total_count = 1
    total_grains = total_count
    for _ in range(2, 65):
        total_count = total_count * 2
        total_grains += total_count
    return total_grains