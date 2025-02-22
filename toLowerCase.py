def toLowerCase(s):
    ordRes = []

    for i in s:
        if ord(i) < 65 or ord(i) > 90:
            ordRes.append(ord(i))
            continue
        
        newOrd = ord(i) + 32
        ordRes.append(newOrd)

    res = ''.join(map(chr, ordRes))
    return res


a = toLowerCase("MixedCASE123" * 8 + "XyZ")
print(a)