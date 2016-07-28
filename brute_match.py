"""
string match algorithm

StringMatch(T[0..n-1], P[0..m-1])
for i <- 0 to n-m do
	j <- 0
	while j < m and p[j] = T[i+j] do 
		j <- 0
		if j = m return i
return -1

"""
def bruteMatch(n, m):
    for i in range(0,len(n)-len(m)+1): # n=sentence m=word
#         print(sentence[i:len(word)+i]) #len(cake) from 0 -> 4 + 0
         if n[i:len(m)+i] == m:
            return(i)
    return -1 
   
sentence = "she shell sea shells by the sea shore."
word = "shell"

ind = bruteMatch(sentence, word)

print(sentence[ind:4+len(word)])