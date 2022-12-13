import numpy as np

def result(m,n):
    '''m = no of outcomes
    n = no of samples'''
    return np.random.randint(1,n+1,m)

# rolling dice
bet=0; 
for i in range(1000):
    res = result(1,6);
    if res == 1:
        bet+=1;
print('dice :',bet/1000)

# head / tail
bet=0; 
for i in range(1000):
    res = result(1,2);
    if res == 1:
        bet+=1;
print('toss :',bet/1000)

