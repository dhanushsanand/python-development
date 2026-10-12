def is_armstrong_number(number):
    digits = count_digits(number)
    sum = 0
    arm_number = number
    while number > 0:
        last_digit = number % 10
        sum += last_digit ** digits
        number //= 10
    return True if arm_number == sum else False

def count_digits(number:int)->int:
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count
