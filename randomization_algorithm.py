"""
Randomization Algorithm - Randomizing an array.

For i = 1 To N
    ' Pick an item for position i.
    j = Random number between i and N
    
    ' Swap items i and j.
    temp = value[i]
    value[i] = value[j]
    value[j] = temp
    
Next i

"""
# python 
from random import randint



alist = [1,2,3,4,5,6]
result = []
n = len(alist)
for i in range(1, n):
    # Pick an item for position i.
    j = randint(i, n-1)


    # Swap items i and j.
    alist[i], alist[j] = alist[j], alist[i]

print(alist)