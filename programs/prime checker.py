def IsPrime(n):
    for i in range(2,n//2):
        if n%i is 0:
            return False
    return True

print('Is prime :',IsPrime(int(input('Enter number :'))))

