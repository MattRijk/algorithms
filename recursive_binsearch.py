def search(x, nums):
    return recBinSearch(x, nums, 0, len(nums)-1)


# recursive binary search
def recBinSearch(x, nums, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    item = nums[mid]
    if item == x:
        return mid
    elif x < item:
        return recBinSearch(x, nums, low, mid-1)
    else:
        return recBinSearch(x, nums, mid+1, high)

    return None

# sorted list
n = [0,1,2,3,5,7,8,12]
search(12, n)