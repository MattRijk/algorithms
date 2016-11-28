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

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
    
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
    return alist