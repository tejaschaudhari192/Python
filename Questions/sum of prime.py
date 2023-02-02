n = int(input("Enter Value : "))

# making list of prime numbers
prime_list = []
for num in range(2, n):
    i = 2
    prime = False
    while i <= num:
        if num % i == 0:
            prime = True
        i += 1
    if prime == True:
        prime_list.append(num)
# print(prime_list)

# addng two prime numbers and checking sum
no = 1
for num1 in range(len(prime_list)):
    for num2 in range(num1, len(prime_list)):
        if (prime_list[num1] + prime_list[num2]) is n:
            print(f"Combination {no} : {prime_list[num1]} + {prime_list[num2]}")
            no += 1
