def failTable(pattern): # fail func
    result = [None]

    for i in range(0, len(pattern)):  
        j = i
        
        while True:
            if j == 0:
                result.append(0)
                break

            if pattern[result[j]] == pattern[i]:
                result.append(result[j] + 1)
                break

            j = result[j]
    
    return result

def kmpMatch(needle, haystack):
    fail = failTable(needle) # fail func

    index = 0
    match = 0

    # Loop until we fall off the string or match.
    while index + match < len(haystack):
        print('{}, {}'.format(index, match))

        if haystack[index + match] == needle[match]:
            match = match + 1
            if match == len(needle):
                return 'index pos: {}'.format(index)
        else:
            if match == 0:
                index = index + 1
            else:
                index = index + match - fail[match]
                match = fail[match]
    return None

p = 'oneb'
t = 'abbabconebabbdasonebsaavaone'
kmpMatch(p, t)