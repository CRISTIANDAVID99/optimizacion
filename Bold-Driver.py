import numpy as np
f = lambda x: 2*np.sin(x)-(x**2)/10
df = lambda x: 2*np.cos(x)-2*x/10
x0=0
u=1
a=0.9
l=1.5
xk=x0

for i in range(10):
    x0=xk
    
    xk=xk+u*df(xk)
    print(x0,xk)
    if(f(xk+u*df(xk))/f(x0))>1:
        u=a*u       
        print("y")
    if(f(xk+u*df(xk))<=f(x0)):
        print("N")
        u=l*u
    
print(xk)
print(u)

