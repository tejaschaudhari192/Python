n = int(input("Enter Value : "))
l = []
while n != 0:
    digit = n % 10
    l.append(digit)
    n = n // 10

print(l)

for in range(len(l))