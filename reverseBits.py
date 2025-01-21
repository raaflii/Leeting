def reverseBits(n):
    n = format(n, 'b')

    zero = ''
    if len(n) != 32:
        for i in range (32 - len(n)):
            zero += '0'

    n = zero + n

    reverse = str(n)[::-1]

    res = 0
    for i in range (len(reverse) - 1, -1, -1):
        res += int(reverse[abs(i - (len(reverse) - 1))]) * 2 ** i

    return res

a = reverseBits(0b00000010100101000001111010011100)
print(a)