"""
for j = 2 to A.length
  key = A[j]
  // Insert A[j] into the sorted sequence A[1 .. j-1]
  i = j
  while i > 0 and A[j - 1] > key
      A[i] = A[i - 1]
      i = i -1
  A[i] = key
"""
def insertSort(alist):
    for j in range(1,len(alist)):
        key = alist[j]
        i = j 
           
        while i > 0 and alist[i-1] > key:
            alist[i] = alist[i-1]
            i = i - 1
        alist[i] = key
            
a = [5,2,4,6,1,3]
insertSort(a)
print(a)