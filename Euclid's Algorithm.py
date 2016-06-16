"""
Euclid's Algorithm

GCD(A, B) 
    While (B <> 0) # As long as b is not 0.
        remainder = A mod B
        ' GCD(A, B) = GCD(B, remainder)
        A = B
        B = remainder
    Loop
    Return A
"""
def GCD(A, B):
    while B != 0:
        remainder = A % B
        'GCD(A, B) = GCD(B, remainder)'
        A, B = B , remainder
    return A

GCD(8, 30)

# def gcd(a, b):
#     """Calculate the Greatest Common Divisor of a and b.

#     Unless b==0, the result will have the same sign as b (so that when
#     b is divided by it, the result comes out positive).
#     """
#     while b:
#         a, b = b, a%b
#     return a