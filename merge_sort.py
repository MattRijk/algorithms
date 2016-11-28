def mergesort(A):
    if len(A) == 1:  
        return A
      
    mid = len(A) // 2  
    left = mergesort(A[:mid])  
    right = mergesort(A[mid:])        
    result = []  
    i = j = 0 
    
    while (len(result) < len(right)+len(left)):          
        if left[i] < right[j]:  
            result.append(left[i])  
            i += 1  
        else:  
            result.append(right[j])  
            j += 1              
        if i == len(left) or j == len(right):              
            result.extend(left[i:] or right[j:])  
            break  
          
    return result


def mergeSort(alist):

    if len(alist) <= 1:
        return alist

    mid = len(alist)//2
    left = alist[:mid]
    right = alist[mid:]

    mergeSort(left)
    mergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            alist[k]=left[i]
            i=i+1
        else:
            alist[k]=right[j]
            j=j+1
        k=k+1

    while i < len(left):
        alist[k]=left[i]
        i=i+1
        k=k+1

    while j < len(right):
        alist[k]=right[j]
        j=j+1
        k=k+1

    return alist

A = [45,63,54,23,2,6,7,8,45]
mergeSort(A)

