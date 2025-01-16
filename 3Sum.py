def threeSum(nums):
    res = []
    for i in range (len(nums)):
        for j in range (i + 1, len(nums)):
            row = []
            for k in range (j + 1, len(nums)):
                if (i != j and i != k and j != k) and (nums[i] + nums[j] + nums[k] == 0):
                    row = [nums[i], nums[j], nums[k]]
                    row.sort()

            if len(row) != 0:
                res.append(row)

    res = [list(x) for x in set(tuple(x) for x in res)]

    return res

a = threeSum([-1,0,1,2,-1,-4])
print(a)