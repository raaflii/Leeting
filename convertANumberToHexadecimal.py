def positiveDecToHex(n):
    hexDict = {
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f'
    }

    if n == 0:
        return str(n)
    
    res = []
    while n > 0:
        rem = n % 16
        n //= 16

        if rem in hexDict.keys():
            rem = hexDict[rem]
        res.insert(0, rem)

    res = ''.join(map(str, res))

    return res

def negativeDecToHex(n):
    max = 4294967295

    if n == -1:
        return positiveDecToHex(max)

    res = max + n + 1

    return positiveDecToHex(res)

def convertANumberToHexadecimal(num):
    if num < 0:
        return negativeDecToHex(num)
    else: 
        return positiveDecToHex(num)

a = convertANumberToHexadecimal(0)
print(a)