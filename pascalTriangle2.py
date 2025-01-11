from math import factorial

def combination(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n - r)))

def pascalTriangle(rowIndex):
    res = []
    for i in range (rowIndex + 1):
        res.append(combination(rowIndex, i))
    return res
    
a = pascalTriangle(3)

print(a)


# combination(6, 3)

    
    
