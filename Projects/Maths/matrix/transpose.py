m = []

for i in range(10):
    x = []
    for j in range(10):
        x.append(0)
    m.append(x)

r = int(input('Enter rows : '))
c = int(input('Enter columns : '))

for i in range(r):
    for j in range(c):
        print(f'Enter elemen {i+1}{j+1} : ')
        m[i][j] =  int(input())

print('Your matrix')
for i in range(r):
    for j in range(c):
        print(m[i][j], end=" ")
    print()
print()

# transpose
print('Transpose matrix')
for i in range(c):
    for j in range(r):
        print(m[j][i], end=" ")
    print()
