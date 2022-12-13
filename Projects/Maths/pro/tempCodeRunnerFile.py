import random

no = 0
n = 60

for i in range(1000):
	bd_seen = []
	
	for p in range(n):
		date = random.randint(1,365);	
		if date not in bd_seen:
			bd_seen.append(date)
		else:
			no += 1;
			break

print('Probablity : ',no/1000)