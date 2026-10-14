def line_up(name, number):
    number_endings = {
        1:"st",
        2:"nd",
        3:"rd"
    }
    last_digit = number % 10
    last_second_digit = (number//10) % 10
    if int(f"{last_second_digit}{last_digit}") in (11, 12, 13):
        return write_message(name, number, "th")
    if last_digit in number_endings.keys():
        return write_message(name, number, number_endings[last_digit])
    return write_message(name, number, "th")

def write_message(name, number, suffix):
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"