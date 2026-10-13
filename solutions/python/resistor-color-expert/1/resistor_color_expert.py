color_map = {
    "black":0,
    "brown":1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}
tolerance_bands = {
    "grey":0.05,
    "violet":0.1,
    "blue":0.25,
    "green":0.5,
    "brown":1,
    "red":2,
    "gold":5,
    "silver":10
}
# print(ord("±"))
GIGA_MULTIPLIER = 1_000_000_000
MEGA_MULTIPLIER = 1_000_000
KILO_MULTIPLIER = 1_000
PLUS_MINUS_SIGN = chr(177)
def resistor_label(colors:list):
    tolerance = tolerance_bands[colors[-1]] if len(colors) > 1 else 0
    resistance_value = 0
    if len(colors) == 4:
        resistance_value = int(f"{color_map[colors[0]]}{color_map[colors[1]]}") * pow(10, color_map[colors[2]])
    elif len(colors) == 5:
        resistance_value = int(f"{color_map[colors[0]]}{color_map[colors[1]]}{color_map[colors[2]]}") * pow(10, color_map[colors[3]])
    
    if 1 <= resistance_value/GIGA_MULTIPLIER < 1000:
        resistance_value = resistance_value/GIGA_MULTIPLIER
        resistance_value = int(resistance_value) if resistance_value.is_integer() else resistance_value 
        return f"{resistance_value} gigaohms {PLUS_MINUS_SIGN}{tolerance}%" if tolerance else f"{resistance_value} gigaohms"
    elif 1 <= resistance_value/MEGA_MULTIPLIER < 1000:
        resistance_value = resistance_value/MEGA_MULTIPLIER
        resistance_value = int(resistance_value) if resistance_value.is_integer() else resistance_value 
        return f"{resistance_value} megaohms {PLUS_MINUS_SIGN}{tolerance}%" if tolerance else f"{resistance_value} megaohms" 
    elif 1 <= resistance_value/KILO_MULTIPLIER < 1000:
        resistance_value = resistance_value/KILO_MULTIPLIER
        resistance_value = int(resistance_value) if resistance_value.is_integer() else resistance_value 
        return f"{resistance_value} kiloohms {PLUS_MINUS_SIGN}{tolerance}%" if tolerance else f"{resistance_value} kiloohms"
    return f"{resistance_value} ohms {PLUS_MINUS_SIGN}{tolerance}%" if tolerance else f"{resistance_value} ohms"


print(resistor_label(["red", "green", "yellow", "yellow", "brown"]))

