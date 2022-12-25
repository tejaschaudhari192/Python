import numpy as np

def uniform(n,m):
    '''m = no of outcomes
    n = no of samples'''
    return np.random.randint(1,n+1,m)

no = 0
for i in range(1):
    cl = uniform(3,1)
    
    if cl == 1:
        g1l = 2; g2l = 3
    if cl == 2:
        g1l = 1; g2l = 3
    if cl == 3:
        g1l = 1; g2l = 2
        
    co = uniform(3,1)
    if co == g1l:
        hrl = g2l;
        ocd = cl
    if co == g2l:
        hrl = g1l;
        ocd = cl;
    if ocd == cl:
        no+=1;

print(np/100)

    