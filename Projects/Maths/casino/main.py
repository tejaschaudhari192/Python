import numpy as np
avg_return = 0

a =1.0;b=4.0
k1=1;k2=1

def draw ():
    s1 = np.random.randint(1,7)
    s2 = np.random.randint(1,7)
    sm = s1 + s2
    return sm


bet = int(input('Enter : '))

for i in range (1000):
    sum = bet
    if sum <= 6 or sum >= 8 :
        avg_return += k1*(a-1)/1000
    if sum is 7 :
        avg_return += k2*(a-1)/1000
    if sum <= 6 or sum >= 8 :
        avg_return += k1*(a-1)/1000
    if sum is 7 :
        avg_return += k1*(a-1)/1000
        
print(avg_return)


# for i in range(1000):
#     bet = draw()
