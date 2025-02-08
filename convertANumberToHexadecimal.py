def hexToDec(n):
    hexaDict = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

    res = 0 #3a
    for i in str(n, -1, -1):
        if i in hexaDict.values():
            i = hexaDict[i]
        res += int(i) * 16**(i)
        return res

def convertANumberToHexadecimal(num):
    

    
