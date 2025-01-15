def plusOne(digits):
    strList = list(map(str, digits))
    intDigits = int(''.join(strList))
    
    intDigits += 1

    res = [int(x) for x in str(intDigits)]
    return res

plusOne([1, 2, 3])