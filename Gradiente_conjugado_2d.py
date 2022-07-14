import numpy as np

f = lambda x,y:((x-y)**2+(x-2)**2+(y-3)**4)/10

df = lambda x,y: np.array([(2*(x-y)+2*(x-2))/10,(-2*(x-y)+4*(y-3)**3)/10])


x0=np.array([0,0])
deff=df(x0[0],x0[1])
xk=x0+deff
d0=-1*df(x0[0],x0[1])
print(xk)
for i in range(2000):

    s0=-1*df(x0[0],x0[1])
    sk=-1*df(xk[0],xk[1])

    bk=(np.dot(np.transpose(sk),sk))/(np.dot(np.transpose(s0),s0))
    print(xk)
    dk=sk+bk*d0
    d0=dk

    x0=xk
    xk=xk+0.0001*dk

print(f(xk[0],xk[1]))