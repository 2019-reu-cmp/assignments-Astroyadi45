'Function integrators'

'Trapezoidal rule'
import numpy as np

def f(x,a=1,b=1):
    return a*x**2 + b*x

x=np.arange(10)

dx= 1 #interval
trap = dx * (f(x + dx) + f(x)) / 2
print(trap)


'Simpsons rule'
a=x[0]
b=x[9]

h = (b - a) / 3
factor = (f(a) +
          3*f((2*a + b) / 3) +
          3*f((a + 2*b) / 3) +
          f(b))
integral = (3 * h / 8) * factor
print(integral)

