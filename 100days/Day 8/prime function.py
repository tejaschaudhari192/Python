def prime_checker(number):
    n = number
    i = 1
    div = 0

    while i <= n:
        if n % i == 0:
            div += 1
        i += 1

    if div == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))

prime_checker(number=n)
