def equilateral(sides):
    if 0 in sides or (sides[0] + sides[1]) < sides[2] or (sides[0] + sides[2]) < sides[1] or (sides[1] + sides[2]) < sides[0]:
        return False
    return sides[0] == sides[1] == sides[2]
    
def isosceles(sides):
    if 0 in sides or (sides[0] + sides[1]) < sides[2] or (sides[0] + sides[2]) < sides[1] or (sides[1] + sides[2]) < sides[0]:
        return False
    return (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2])

def scalene(sides):
    if 0 in sides or (sides[0] + sides[1]) < sides[2] or (sides[0] + sides[2]) < sides[1] or (sides[1] + sides[2]) < sides[0]:
        return False
    return (sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2])
