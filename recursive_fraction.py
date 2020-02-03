#Elaine Lee
#Dec 2019
'''Weird fraction n + 1/(n-1 + 1/(n-2 + ...))'''

from math import *

def comp_fract(c, n):
    if n <= 1:
        return c[0]
    else:
        return c[n-1] + (1/(comp_fract(c, n-1)))
                         

                         
if __name__ == "__main__":
    a = [i for i in range(1,11)]
    print("Fraction: ", (comp_fract(a, len(a))))
