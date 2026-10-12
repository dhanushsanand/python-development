def equilateral(sides):
    if triangle_inequality(sides):
        a, b, c = sides
        return True if a == b == c else False    
    return False

def triangle_inequality(sides):
    a, b, c = sides
    if (a + b > c) and (b + c > a) and (c + a) > b:
        return True
    return False

def isosceles(sides):
    if triangle_inequality(sides):
        a, b, c = sides
        if a == b or b == c or c == a:
            return True
        return False
    return False


def scalene(sides):
    if triangle_inequality(sides):
        a, b, c = sides
        if (a != b) and (b != c) and (c != a):
            return True
        return False
    return False
