n = int(input("Enter Value : "));
sum =0;

for i in range(1,n//2 + 1):
    if n%i is 0:
        sum+= i

if sum is n :
    print('yes')
else:
    print('no')