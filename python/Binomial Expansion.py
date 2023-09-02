"""
The purpose of this Kata is to write a program that can do some algebra. Write a function expand that
takes in an expression with a single, one character variable, and expands it. The expression is in the 
form (ax + b)^n where a and b are integers which may be positive or negative, x is any single character 
variable, and n is a natural number. If a = 1, no coefficient will be placed in front of the variable.
If a = -1, a "-" will be placed in front of the variable.

The expanded form should be returned as a string in the form ax^b + cx^d + ex^f... where a, c, and e are 
the coefficients of the term, x is the original one character variable that was passed in the original 
expression and b, d, and f, are the powers that x is being raised to in each term and are in decreasing 
order. If the coefficient of a term is zero, the term should not be included. If the coefficient of a term
is one, the coefficient should not be included. If the coefficient is -1, only the "-" should be included. 
If the power of the term is 0, only the coefficient shouold be included. If the power of the term is 1,
the caret and power should be excluded

Examples:
    expand("(x+1)^2")      # returns "x^2+2x+1"
    expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
    expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
    expand("(-2a-4)^0")    # returns "1"
    expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
    expand("(r+0)^203")    # returns "r^203"
    expand("(-x-1)^2")     # returns "x^2+2x+1"
"""

import re

P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')

def expand(expr):
    a,v,b,e = P.findall(expr)[0]

    if e == '0': 
        return '1'
    
    o = [int(a != '-' and a or a and '-1' or '1'), int(b)]
    e, p = int(e), o[:]

    for _ in range(e - 1):
        p.append(0)
        p = [o[0] * coef + p[i - 1] * o[1] for i, coef in enumerate(p)]
    
    res = '+'.join(f'{coef}{v}^{e-i}' if i != e else str(coef) for i, coef in enumerate(p) if coef)

    return re.sub(r'\b1(? = [a - z])|\^1\b', '', res).replace('+-', '-')