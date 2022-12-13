import random
import numpy as np

no =0
n =60
print('Finding probab;ity for same bday of two persons in room')
print('\nBy formula :',1 - np.prod(1-np.arange(365/n)))
print('\nBy morto carlo simulation :')

for i in range(1000):
	bd_seen = []
	
	for p in range(n):
		date = random.randint(1,365);	
		if date not in bd_seen:
			bd_seen.append(date)
		else:
			no += 1;
			break
P = no/1000
print('Probablity : ',P)
print(f'{P*100}% ')

#coded by tejas