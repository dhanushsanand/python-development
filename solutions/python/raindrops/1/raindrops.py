from operator import mod
def convert(number):
    raindrop_sound = ""
    if mod(number, 3) == 0:
        raindrop_sound += "Pling"
    if mod(number, 5) == 0:
        raindrop_sound += "Plang"
    if mod(number, 7) == 0:
        raindrop_sound += "Plong"
    return f"{number}" if len(raindrop_sound) == 0 else raindrop_sound

