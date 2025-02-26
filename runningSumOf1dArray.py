def runningSum(nums):
    res = []
    
    sumNums = 0

    for i in nums:
        sumNums += i
        res.append(sumNums)

    return res

a = runningSum([0,0,0,0])
print(a)