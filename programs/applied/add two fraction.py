x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

numerator = x1 * y2 + x2 * y1
denominator = y1 * y2

if numerator > denominator:
    div = denominator
else:
    div = numerator

for i in range(div, 1, -1):
    if denominator % i is 0 and numerator % i is 0:
        numerator = numerator // i
        denominator = denominator // i

print("Addition :")
if denominator is 1:
    print(numerator)
else:
    print(numerator, "/", denominator)
