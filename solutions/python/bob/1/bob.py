def response(hey_bob:str):
    hey_bob = hey_bob.strip()
    if len(hey_bob) == 0:
        return "Fine. Be that way!"

    if hey_bob.endswith("?"):
        is_yell = hey_bob[:-1]
        if is_yell.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    
    # if hey_bob.isspace():
    #     return "Fine. Be that way!"
    return "Whatever."

#print(response("HeY, WHATS UP?"))

# string = "HEY, WHATS UP?"[:-1]
# print(string)
# print(string.isupper())