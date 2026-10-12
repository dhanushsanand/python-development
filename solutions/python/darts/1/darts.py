import math
def score(x, y):
    circle_radius = math.sqrt(pow(x, 2)+ pow(y, 2))

    if circle_radius <= 1:
        return 10
    if 1 < circle_radius <= 5:
        return 5
    if 5 < circle_radius <= 10:
        return 1
    return 0
