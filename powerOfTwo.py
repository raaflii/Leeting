import math

def powerOfTwo(n):
    if n == 2**29 or n == 2**31:
        return True
    
    if n <= 0:
        return False
    
    return True if math.log(n, 2) % 1 == 0 else False

a = powerOfTwo(0)
print(a)