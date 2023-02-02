n = int(input("Enter number : "))

i = 1
div = 0

while i <= n:
    if n % i == 0:
        div += 1
    i += 1

print(f"div = {div}")

if div == 2:
    print("prime")
else:
    print("Not prime")
    







