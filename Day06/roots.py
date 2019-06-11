'Root finders'
import numpy as np

def f(x,a=1,b=0):
    return a*x**2 + b*x

'Newtons method'

def f_prime(x,a=1): #if function is f(x)=x^2
    return 2*a*x
x_init=1
new_x=x_init-(f(x_init)/f_prime(x_init))
diff=x_init-new_x

while (diff>1e-5):   
    new_x=x_init-(f(x_init)/f_prime(x_init))
    diff=x_init-new_x
    x_init=new_x #update values
    print(new_x)
    

'Secant Method'
x0=0
x1=1
x2 = x1 - f(x1) * (x1 - x0)/( f(x1) - f(x0) )
diff=x2-x1
t=0
while (diff>1e-5):
    x_new=[]
    x2 = x1 - f(x1) * (x1 - x0)/( f(x1) - f(x0) )
    diff=x2-x1
    x_new.append(x2)
    x0=x1 #update values
    x1=x_new[t]
    t+=1
    print(x2)
