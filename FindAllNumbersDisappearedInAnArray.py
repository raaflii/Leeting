def findDisappearedNumbers(nums):
    res = []
    setNums = set(nums)

    for i in range(1, len(nums) + 1):
        if i not in setNums:
            res.append(i)
    
    return res

a = findDisappearedNumbers([11])
print(a)