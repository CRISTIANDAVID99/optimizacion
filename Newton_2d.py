import numpy as np

import numpy as np

f = lambda x,y:((x-y)**2+(x-2)**2+(y-3)**4)/10

df = lambda x,y: np.array([(2*(x-y)+2*(x-2))/10,(-2*(x-y)+4*(y-3)**3)/10])

d2f = lambda x,y: np.array([[(2+2)/10,(-2)/10],[(2)/10,(-2+12*(y-3)**2)/10]])


xl=0
xk=np.array([0,0])
for i in range(1000):

    dk=-np.dot(np.linalg.inv(d2f(xk[0],xk[1])),df(xk[0],xk[1]))
    xk=xk+dk

print(xk)