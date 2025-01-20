def reverseBits(n):
    reverse = str(n)[::-1]
    print(reverse)

    res = 0
    for i in range (len(reverse) - 1, -1, -1):
        print(i)
        res += int(reverse[abs(i - (len(reverse) - 1))]) * 2 ** i

    return res

a = reverseBits("00000010100101000001111010011100")
print(a)