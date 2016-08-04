#!/bin/python3

import sys


# a0,a1,a2 = input().strip().split(' ')
# a0,a1,a2 = [int(a0),int(a1),int(a2)]
# b0,b1,b2 = input().strip().split(' ')
# b0,b1,b2 = [int(b0),int(b1),int(b2)]

a = [5,6,7]
b = [3,6,10]



def counter(a, b):
    x = 0
    y = 0
    for i in range(3):
        if a[i] > b[i]:
            x += 1
        elif a[i] < b[i]:
            y += 1
    return '{0} {1}'.format(x, y)



counter(a,b)