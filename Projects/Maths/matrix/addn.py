r1 = int(input('Enter rows of first matrix : '))
c1 = int(input('Enter columns of first matrix : '))
r2 = int(input('\nEnter rows of second matrix : '))
c2 = int(input('Enter columns of second matrix : '))

if (r1 != r2) or (c1 != c2):
    print('invalid input')
    exit()
else:
    f = r1

print('Enter elements of matrix [A] : ')
a = []
for r in range(r1):
    r = []
    for i in range(c1):
        r.append(int(input()))
    a.append(r)

print(a)

# second matrix

print('Enter elements of matrix [B] : ')
b = []
for r in range(r2):
    r = []
    for i in range(c2):
        r.append(int(input()))
    b.append(r)

print(b)

# matrix addition
c = []
for i in range(r1):
    r = []
    for j in range(c1):
        r.append(a[i][j]+b[i][j])
    c.append(r)

print('\n[A] + [B] :')


# formatted output
for i in range(r1):
    for j in range(c1):
        print(c[i][j], end=" ")
    print()

