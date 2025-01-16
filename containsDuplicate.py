def containsDuplicate(nums):
    setNums = set()

    for i in nums:
        setNums.add(i)
    
    if len(nums) != len(setNums):
        return True
    else:
        return False

a = containsDuplicate([1,2,3,1])
print(a)    