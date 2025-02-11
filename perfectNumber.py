def perfectNumber(num):
    if num == 1:
        return False
    
    res = 1
    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:
            res += i + (num / i)
        if res > num:
            return False

    if res == num:
        return True
    return False

a = perfectNumber(33550336)
print(a)