from math import factorial

def combination(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n - r)))

def pascalTriangle(numRows):
    res = []
    for i in range (numRows):
        row = []
        for j in range (i + 1):
            row.append(combination(i, j))
        res.append(row)
    return res
    

a = pascalTriangle(5)

print(a)


# combination(6, 3)

    
    
