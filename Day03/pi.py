#!/usr/bin/env python3
""" pi.py - 
"""
import math as m

def srinivasa(k):
    """
    """
    i=0
    calc=0
    cst=(2*m.sqrt(2)/9801)
    while i<k:
        print(i)
        calc+=float((m.factorial(4*i)*(1103+(26390*i)))/((m.factorial(i)**4)*396**(4*i)))
        i+=1
        print(k)
        print(calc)
    pi_calc=1/(cst*calc)
    acc=pi_calc-m.pi
    print(acc)
    return pi_calc

if __name__ == '__main__':
    iterations = 3
    print(srinivasa(iterations))
    
