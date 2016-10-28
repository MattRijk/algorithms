# Python Linear Search in O(n)
"""
Forward Search
For each item in the list:
     if that item has the desired value,
         stop the search and return the item's location.
 Return Λ.
 
Set i to 1.
 Repeat this loop:
     If i > n, then exit the loop.
     If A[i] = x, then exit the loop.
     Set i to i + 1.
 Return i
"""

"""
 LinearSearch(value, list)
   if the list is empty, return Λ;
   else
     if the first item of the list has the desired value, return its location;
     else return LinearSearch(value, remainder of the list)
"""

A = ['one', 'two', 'three', 'four', 'five']

def linsearch(A, target):
    for i in A:
        if i == target:
            return A.index(i)
    return 0


# recursive linear search
def rsearch(A, target, i=None):
    if i is None: 
        i = len(A) - 1
    if i < 0: 
        return None
    if target == A[i]: 
        return i
    return rsearch(A, target, i-1)

print(linsearch(A, 'three'))
print(rsearch(A, 'one'))