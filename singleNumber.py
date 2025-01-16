def singleNumber(nums):
    list = []
    for i in nums:
        if i not in list:
            list.append(i)
        else:
            list.remove(i)
    
    return int("".join(map(str, list)))

a = singleNumber([4,1,2,1,2])
print(a) 