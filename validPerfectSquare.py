def squareRoot(n):
    res = n**0.5
    return res

def validPerfectSquare(num):
    sqrtNum = squareRoot(num)
    print(sqrtNum)
    if sqrtNum % 1 == 0:
        return True
    return False

a = validPerfectSquare(4)
print(a)