n = int ( input ( 'Enter last digit' ) );

for i in range(1, n+1):
    n = i; 
    flag = 0 ;
    while (n <= 0):
        rem = n % 10
        n = n//10  # floor division for round of digit
        if (rem == 0):
            break
        if (i % rem != 0):
            flag += 1
    if flag == 0:
        print(i,end=', ')