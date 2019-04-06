
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    c = 0
    print(nums)
    for n in nums:
        if n != val:
            # nums[c] = n
            c += 1
    print(nums)
    print(c)
    return c


nums = [3, 2, 2, 3]
val = 3

removeElement(nums, val)