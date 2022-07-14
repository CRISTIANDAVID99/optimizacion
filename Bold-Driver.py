import numpy as np
f = lambda x: 2*np.sin(x)-(x**2)/10
df = lambda x: 2*np.cos(x)-2*x/10
x0=2
u=0.1
a=0.7
l=1.5
xk=x0

for i in range(100000):
    x0=xk
    xk=xk-u*df(xk)
    if(f(xk+u*df(xk))/f(x0))>=1.04:
        u=a*u
    if(f(xk+u*df(xk))<f(x0)):
        
        u=l*u
    
print(xk)

