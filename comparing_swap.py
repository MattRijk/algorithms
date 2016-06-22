code:

import dis

def swap1():
  a=5
  b=4
  a, b = b, a

def swap2():
  a=5
  b=4
  c = a
  a = b
  b = c

print 'swap1():'
dis.dis(swap1)
print 'swap2():'
dis.dis(swap2)
output:

swap1():
  6           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (a)

  7           6 LOAD_CONST               2 (4)
              9 STORE_FAST               1 (b)

  8          12 LOAD_FAST                1 (b)
             15 LOAD_FAST                0 (a)
             18 ROT_TWO             
             19 STORE_FAST               0 (a)
             22 STORE_FAST               1 (b)
             25 LOAD_CONST               0 (None)
             28 RETURN_VALUE        
swap2():
 11           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (a)

 12           6 LOAD_CONST               2 (4)
              9 STORE_FAST               1 (b)

 13          12 LOAD_FAST                0 (a)
             15 STORE_FAST               2 (c)

 14          18 LOAD_FAST                1 (b)
             21 STORE_FAST               0 (a)

 15          24 LOAD_FAST                2 (c)
             27 STORE_FAST               1 (b)
             30 LOAD_CONST               0 (None)
             33 RETURN_VALUE        
Two loads, a ROT_TWO, and two saves, versus three loads and three saves. You are unlikely to find a faster mechanism.