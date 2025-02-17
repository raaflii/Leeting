def selfDividingNumbers(left, right):
    res = []


    for i in range (left, right + 1):
        for j in str(i):
            if i % j != 0:
                continue
        
                

a = selfDividingNumbers(47, 85)
print(a)
        