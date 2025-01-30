def searchInsertPosition(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid] :
            low = mid + 1
        else:
            return mid
    
    if target < nums[mid]:
        return mid
    else:
        return mid + 1

a = searchInsertPosition([1,3], 2)
print(a)
    

    