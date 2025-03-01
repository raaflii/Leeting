def sumAllDigits(a):
    sum = 0
    for i in str(a):
        sum += int(i)
    return sum

def addDigits(num):
    if num == 0:
        return 0
    
    sumRes = sumAllDigits(num)
    while len(str(sumRes)) != 1 or sumRes == 0:
       sumRes = sumAllDigits(sumRes)
    return sumRes

a = addDigits(19)
print(a)