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

def label(colors):
    # color_1 = colors[0]
    # color_2 = colors[1]
    ohms = color_map[colors[2]]
    resistor_value = int(f"{color_map[colors[0]]}{color_map[colors[1]]}")
    ohms_label = resistor_value * pow(10, ohms)
    if ohms_label == 0:
        return f"0 ohms"
    if ohms_label % 1000000000 == 0:
        resistor_value = ohms_label//1000000000
        return f"{resistor_value} gigaohms"
    if ohms_label % 1000000 == 0:
        resistor_value = ohms_label//1000000
        return f"{resistor_value} megaohms"
    if ohms_label % 1000 == 0:
        resistor_value = ohms_label//1000
        return f"{resistor_value} kiloohms"
    return f"{ohms_label} ohms"

    
