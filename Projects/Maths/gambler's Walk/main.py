import numpy
no = 0

def Draw(m, n):
    """m = lower bound
    n = upper bound"""
    return numpy.random.randint(m, n + 1)

k = 5
N = 10
print('Probablity by using formula =',1-k/N)

for i in range(1000):
    k = 5
    while k is not 0 and k < N:
        bet = Draw(1,2)
        if bet is 1:
            k += 1
        else:
            k -= 1
        if k is 0:
            no += 1
print('Probablity using monto carlo =',no / 1000)
