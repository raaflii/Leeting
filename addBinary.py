def binaryToDecimal(binary):
    decimal = 0
    for i in range (len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * 2 ** (len(binary) - (i + 1))

    return decimal

def addBinary(a, b):
    a = binaryToDecimal(a)
    b = binaryToDecimal(b)

    res = format((int(a) + int(b)), 'b')
    return res

a = addBinary("11010101011", "10101010101")
print(a)

