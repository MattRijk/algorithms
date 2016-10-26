def heapsort( alist ):
    # convert alist to heap
    length = len( alist ) - 1
    leastParent = length // 2

    for i in range ( leastParent, -1, -1 ):
        moveDown( alist, i, length )

    # flatten heap into sorted array
    for i in range ( length, 0, -1 ):
        if alist[0] > alist[i]:
            swap( alist, 0, i )
            moveDown( alist, 0, i - 1 )
            
    return alist

def moveDown( alist, first, last ):
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if ( largest < last ) and ( alist[largest] < alist[largest + 1] ):
            largest += 1

        # right child is larger than parent
        if alist[largest] > alist[first]:
            swap( alist, largest, first )
            # move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return None  # force exit


def swap( A, x, y ):
    A[x], A[y] = A[y], A[x]

    
heapsort([7,8,4,5,9,3,2])

# output
# [2, 3, 4, 5, 7, 8, 9]
