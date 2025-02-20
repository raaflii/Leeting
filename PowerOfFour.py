def powerOfFour(n):
    if n < 0:
        return False
    
    for i in range (int(n**0.25) + 2):
        if 4**i == n:
            return True
    return False

num = 4**3
a = powerOfFour(num)
print(a)