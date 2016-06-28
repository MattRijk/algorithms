"""
Binary Search Summary
Best: O(1) Average, Worst: O(log n)
search (A,t)
    low = 0
    high = n-1
    while low ≤ high do
        mid = (low + high)/2
        if t < A[mid] then
            high = mid - 1
        else if t > A[mid] then
            low = mid + 1
        else
            return true
    return false
end

Repeat while there is a range to be searched.

Midpoint computed using integer arithmetic.

“Variations” on page 99 discusses how to support

"""



def binarySearch(theValues, target):
     # Start with the entire sequence of elements
    low = 0
    high = len(theValues) - 1
    
     # Repeatedly subdibide the sequence in half until the target is found
    while low <= high:
         # Find the midpoint of the sequence
        mid = (high+low) // 2
         # Does the midpoint contain the target?
        if theValues[mid] == target:
            return True
         # or does the target precede the midpoint?
        elif target < theValues[mid]:
            high = mid - 1
         # Or does it follow the midpoint?
        else:
            low = mid + 1

     # If the sequence cannot be subdibided further, we're done
    return False

# Example two
def binarysearch(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        item = nums[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1           
        else:
            low = mid + 1
            
    return False

# sorted list
n = [0,1,2,3,4,5,6,7,12,14]
binarysearch(12, n)

