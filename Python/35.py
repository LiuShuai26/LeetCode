# 简单二分搜索

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = int((low+high)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return low


print(searchInsert([1, 3, 4, 6, 7, 9], 5))
