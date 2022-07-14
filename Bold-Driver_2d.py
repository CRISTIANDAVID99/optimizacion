import numpy as np

f = lambda x,y:((x-y)**2+(x-2)**2+(y-3)**4)/10

df = lambda x,y: np.array([(2*(x-y)+2*(x-2))/10,(-2*(x-y)+4*(y-3)**3)/10])

x0=np.array([0,0])

u=0.1
a=0.7
l=1.5

xk=x0

for i in range(100000):
    x0=xk
    xk=xk-u*df(xk[0],xk[1])
    xkn=xk+u*df(xk[0],xk[1])
    if(f(xkn[0],xkn[1])/f(x0[0],x0[1]))>=1.04:

        u=a*u

    if(f(xkn[0],xkn[1])<f(x0[0],x0[1])):
        
        u=l*u
    
print(xk)
