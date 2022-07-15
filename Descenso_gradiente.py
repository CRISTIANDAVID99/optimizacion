import numpy as np
f = lambda x: 2*np.sin(x)-(x**2)/10
df = lambda x: 2*np.cos(x)-2*x/10
xh=4
xl=0
xk=2
for i in range(1000):
    if(xk>=xh):
        xk=xh
    else:
        xk=xk+0.01*df(xk)
print(xk)

