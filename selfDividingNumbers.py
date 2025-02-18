def selfDividingNumbers(left, right):
    res = []

    while left <= right:
        cond = True

        if '0' in str(left):
            left += 1
            continue

        listNum = list(str(left))

        for i in listNum:
            if left % int(i) != 0:
                cond = False
                break
        
        if cond == True:  
            res.append(left)

        left += 1

    return res
        

a = selfDividingNumbers(1, 22)
print(a)
        