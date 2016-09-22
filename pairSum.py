def pairSum(arr, target):
    if len(arr)<= 2:
        raise ValueError('Enter three or more values')
    arr.sort()
    left, right = (0, len(arr) - 1)
    while left < right:
        currentSum=arr[left] + arr[right]
        if currentSum == target:
            print(arr[left], arr[right])
            left += 1 #or right-=1
        elif currentSum < target:
            left += 1
        else:
            right -= 1

pairSum([1,2,3,4,5,6,8,9], 10)