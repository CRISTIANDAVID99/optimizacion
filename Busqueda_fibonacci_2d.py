from matplotlib.pyplot import ylabel
import numpy as np
from functools import reduce

xh=10
xl=-10
yh=10
yl=-10
for n in range(1,1000):
    
    fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
    dk=(fib(n-2)/fib(n))*(xh-xl)
    f = lambda x,y:((x-y)**2+(x-2)**2+(y-3)**4)/10
    #print(dk)
    x1=xl+dk
    x2=xh-dk
    y1=yl+dk
    y2=yh-dk
    x=(x1+x2)/2
    y=(y1+y2)/2

    if(f(x,y1)>=f(x,y2)):
        yl = y1    
    else:
        yh = y2

    if(f(x1,y)>=f(x2,y)):
        xl = x1    
    else:
        xh = x2

    
print((xh+xl)/2)
print((yh+yl)/2)

print(f((xh+xl)/2,(yh+yl)/2))
       
