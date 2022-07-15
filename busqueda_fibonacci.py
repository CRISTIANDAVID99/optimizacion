from matplotlib.pyplot import ylabel
import numpy as np
from functools import reduce

xh=4
xl=0
yh=4
yl=0
for n in range(1,1000):
    
    fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
    dk=(fib(n-2)/fib(n))*(xh-xl)
    #print(dk)
    x1=xl+dk
    x2=xh-dk


    fx1 = 2*np.sin(x1)-(x1**2)/10
    fx2 = 2*np.sin(x2)-(x2**2)/10


    if(fx1>=fx2):
        
        xh = x2  
    else:
         xl = x1 

print((xh+xl)/2)
print(2*np.sin((xh+xl)/2)-(((xh+xl)/2)**2)/10)
       
