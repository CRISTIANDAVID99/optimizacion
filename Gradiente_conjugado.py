import numpy as np
f = lambda x: 2*np.sin(x)-(x**2)/10
df = lambda x: 2*np.cos(x)-2*x/10
xh=4
xl=0
x0=0
xk=x0+df(x0)
d0=-df(x0)
print(xk)
for i in range(60):

    s0=-df(x0)
    sk=-df(xk)

    bk=(sk**2)/(s0**2)

    dk=sk+bk*d0
    d0=dk

    x0=xk
    xk=xk+0.01*dk

    print(xk)
print(f(xk))