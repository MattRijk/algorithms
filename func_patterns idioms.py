

# efficent fib
def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n]
    return res

# dict set of counters
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
histogram('parrot')
# The counting pattern
count = 0
for i in range(0,len(items),1):
	count += 1

# The filtered-count pattern
count = 0
for i in range(0,len(items),1):
	if (items[i] % 2 == 0):
		count += 1		

# The accumulate pattern
total = 0
for i in range(0,len(items),1):
	total += items[i]
		
# The filtered-accumulate pattern
def sumEvens(items):
	total = 0
	for i in range(0,len(items),1):
		if (items[i] % 2 == 0):
			total += items[i]
	return total

	
# The search pattern	
def find(target,items): # is target in items?
	return occurrences(target,items) > 0
	
def occurrences(target,items):
	count = 0
	for i in range(0,len(items),1):
		if (items[i] == target):
			count = count + 1
	return count

def find(target,items):
	for i in range(0,len(items),1):
		if (items[i] == target):
			return True # short-circuit!
	return False
	
# The extreme pattern
largest = items[0]
for i in range(0,len(items),1): #start comparing at index 1
	if (items[i] > largest):
		largest = items[i]	

# The extreme-index pattern
ilargest = 0
for i in range(1,len(items),1):
	if (items[i] > items[ilargest]):
		ilargest = i	

# The Filter pattern
def extractEvens(items):
	evens = []
	for i in range(0,len(items),1):
		if (isEven(items[i])):
			evens = evens + [items[i]] # array concatenation
	return evens			

	
# The map pattern
def map(f,items):
	result = []
	for i in range(0,len(items),1):
		transformed = f(items[i])
		result.append(transformed)
	return result

# The shuffle pattern
def shuffle(array1,array2):
	array3 = []
	for i in range(0,len(array1),1):
		array3.append(array1[i])
		array3.append(array2[i])
	return array3
	
# The merge pattern
def merge(array1,array2):
	array3 = []
	i = 0
	j = 0
	while (i < len(array1) and j < len(array2)):
		if (array1[i] < array2[j]):
			array3.append(array1[i])
			i = i + 1
		else:
			array3.append(array2[j])
			j = j + 1
	return array3 + array1[i:] + array2[j:]	
	
## anti patterns

# The fossilized pattern
i = 0
while (i < n): # infinite loop
	print(i)
	
# The missed-condition pattern
i = n
while (i > 0): 
	print(i)
	i += 1
	
# The bottomless pattern
def div2(n): # recursion: the base case is never reached
	if (n == 0):
		return 0
	else:
		return 1 + div2(n - 2)

# check duplicates in string
def all_unique(s): 
    x = len(s)
    y = len(set(s))
    
    if x == y :
        return True
    return False
	
	
'''
pseudo code open, while, close pattern
open the file
read the first item
while the read was good
	process the item
	read the next item
close the file
'''
	
## recursive patterns

# The counting pattern
def head(items): return items[0]
def tail(items): return items[1:] #slicing, which copies!

def count(items):
	if (items == []): # base case
		return 0
	else:
		return 1 + count(tail(items))
			
# The accumulate pattern
def head(items): return items[0]
def sum(items):
	if (items == None): #base case
		return 0
	else:
		return head(items) + sum(tail(items))
			
# Filtered-accumulate patterns			
def countEvens(items):
	if (items == None): #base case
		return 0
	elif (head(items) % 2 == 0):
		return 1 + countEvens(tail(items))
	else:
		return 0 + countEvens(tail(items))

# filtered-count
def occurrences(target,items):
	if (items == None):
		return 0
	elif (head(items) == target):
		return 1 + occurrences(target,tail(items))
	else:
		return occurrences(target,tail(items))	
			
# The filter pattern		
def extractEvens(items):
	if (items == None):
		return None
	elif (isEven(head(items))):
		return join(head(items),extractEvens(tail(items)))
	else:
		return extractEvens(tail(items))
			
			
# The map pattern
def map(f,items):
	if (items == None):
		return None
	else:
		return join(f(head(items)),map(f,tail(items)))
	
# The search pattern
def find(target,items):
	if (items == None):
		return False
	elif (head(items) == target): # short-circuit!
		return True
	else:
		return find(target,tail(items))
			
# The merge pattern			
def merge(list1,list2):
	if (list1 == None):
		return list2
	elif (list2 == None):
		return list1
	elif (head(list1) < head(list2)):
		return join(head(list1),merge(tail(list1),list2))
	else:
		return join(head(list2),merge(list1,tail(list2)))
	
# Count char in string
def count_str(s, target):
    if s == '': return 0
    lastnum = s[-1]
    if lastnum == target:
        return count_str(s[:-1], target) + 1
    return count_str(s[:-1], target) + 0
count_str('vvwwwyyxxvvv', 'y')

# Sum digits
def sum_digits(num):
    if num == 0: return 0
    return sum_digits(num/10) + num % 10

# Sum elements in a list
def sum_list(alist):
    if len(alist) == 1: 
        return alist[0]
    else:
        return alist[0] + sum_list(alist[1:])

# recursive patterns
def triangle_numbers(n):
    if n == 0: return 0
    return triangle_numbers(n-1)+n * '#'
	
	for n in range(20):
		print(triangle_numbers(n))
			
			
	
# Swap keys and values in a dictionary
a = {'a': 1, 'b': 2, 'c': 3}
print(a)
{'a': 1, 'c': 3, 'b': 2}
b = {v:k for k, v in a.items()}
print(b)
{1: 'a', 2: 'b', 3: 'c'}

# Filter a dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

a = {k: v for k, v in d.items() if v > 2}
print(a)
{'c': 3, 'd': 4}

names = ['mark', 'henry', 'matthew', 'paul',
         'luke', 'robert', 'joseph', 'carl', 'michael']

		 
# Grouped by length
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

# result: d = {4: ['mark', 'paul', 'luke', 'carl'], 
#              5: ['henry'], 6: ['robert', 'joseph'], 7: ['matthew', 'michael']}

