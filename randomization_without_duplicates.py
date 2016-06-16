from random import randint



"""
num_picked = 0
Do While(num_picked < 5)
    ' Pick a person.
    i = Random number between 1 and N
    
    ' See if we've picked this person before.
    If (Not picked[i]) Then
        ' Pick this person.
        picked[i] = True
        num_picked = num_picked + 1
    End If 
Loop

"""
alist = []
num_picked = 0
while(num_picked < 5):
    i = randint(1, 11)
    
    if i not in alist:
        alist.append(i)
        num_picked += 1
        
print(alist)