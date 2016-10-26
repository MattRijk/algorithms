# naive pattern matching
def match(pattern, text):
    contains_text = False
    t_index = 0
    p_index = 0
    
    while t_index < len(text) and not contains_text:
        if pattern[p_index] == text[t_index]:
            p_index += 1
            if p_index == len(pattern):
                contains_text = True
        else:
            if p_index > 0:
                p_index = 0 

        t_index += 1
    return contains_text

t = 'baaaabbbabbaab'
p = 'bbbbb'
    
print(match(p, t))



# Knuth-Morris-Pratt string matching

from __future__ import generators

def KnuthMorrisPratt(text, pattern):

    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos

t = 'abbababbbabbananab'
p = 'abb'
for s in KnuthMorrisPratt(t, p): 
    print('index pos: {}'.format(s))