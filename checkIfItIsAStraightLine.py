def checkStraightLine(coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dx = x1 - x0
    dy = y1 - y0

    for i in range(2, len(coordinates)):
        xi, yi = coordinates[i]
        if (xi - x0) * dy != (yi - y0) * dx:
            return False
    return True

a = checkStraightLine([[0,0], [1,1], [3,3]])
print(a)



