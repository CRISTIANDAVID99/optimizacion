import numpy as np
f = lambda x: 2*np.sin(x)-(x**2)/10
df = lambda x: 2*np.cos(x)-2*x/10
d2f = lambda x: -2*np.sin(x)-2/10
xh=4
xl=0
xk=0
for i in range(100):

    dk=-df(xk)/d2f(xk)
    xk=xk+dk

print(xk)