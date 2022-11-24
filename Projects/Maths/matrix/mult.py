r1 = int(input('Enter rows of first matrix : '))
c1 = int(input('Enter columns of first matrix : '))
r2 = int(input('\nEnter rows of second matrix : '))
c2 = int(input('Enter columns of second matrix : '))

if (c1 != r2):
    print('invalid input')
    exit()

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





# matrix multiplication
d = []
for c in range(r1):
    x = []
    for r in range(c2):
        e = 0
        for k in range(c1):
            e += a[c][k]*b[k][r]
        x.append(e)
    d.append(x)
print(d)

# formatted output
print('\n[A] * [B] :')
for i in range(r1):
    for j in range(r1):
        print(d[i][j], end=" ")
    print()
