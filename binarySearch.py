def binarySearch (nums, target):
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
    
    return -1

a = binarySearch([-1,0,3,5,9,12], 2)
print(a)