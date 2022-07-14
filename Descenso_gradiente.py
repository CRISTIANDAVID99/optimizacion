import numpy as np
f = lambda x: 2*np.sin(x)-(x**2)/10
df = lambda x: 2*np.cos(x)-2*x/10
xh=4
xl=0
xk=2
for i in range(100):
    if(xk>=xh):
        xk=xh
    else:
        xk=xk+df(xk)
    print(xk)
print(f(xk))
