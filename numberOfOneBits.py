def decToBinary(dec):
    res = []
    while dec > 0:
        rem = dec % 2
        dec //= 2
        res.insert(0, rem)

    res = ''.join(map(str, res))
    return res
    

def numberOfOneBits(n):
    n = decToBinary(n)
    result = 0
    for i in n:
        if i == '1':
            result += 1
    return result

num = 2**31-1
print(num)
a = numberOfOneBits(num)
print(a)
        
