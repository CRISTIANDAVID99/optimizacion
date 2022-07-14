import numpy as np

f = lambda x,y:((x-y)**2+(x-2)**2+(y-3)**4)/10
dfx = lambda x,y:(2*(x-y)+2*(x-2))/10
dfy = lambda x,y:(-2*(x-y)+4*(y-3)**3)/10


xk=0
yk=0
for i in range(1000):

    xk=xk-0.1*dfx(xk,yk)
    yk=yk-0.1*dfy(xk,yk)
    
    print(xk)
    print(yk)
    
print(f(xk,yk))