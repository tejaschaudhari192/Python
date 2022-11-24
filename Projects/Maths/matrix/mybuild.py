from os import system

def MatAdd(a, b, row_a, colm_a, row_b, colm_b):
    '''Function to Add Matrix 
    arguments := rows and colums of both matrix'''
    c = []
    for i in range(row_a):
        r = []
        for j in range(colm_a):
            r.append(a[i][j]+b[i][j])
        c.append(r)
        
    print('\n[A] + [B] =')
    for i in range(row_a):
        for j in range(colm_a):
            print(c[i][j], end=" ")
        print()

def MatMult(a, b, row_a, colm_a, row_b, colm_b):
    '''Function to multiply Matrix 
    arguments := rows and colums of both matrix'''
    d = []
    for c in range(row_a):
        x = []
        for r in range(colm_b):
            e = 0
            for k in range(colm_a):
                e += a[c][k]*b[k][r]
            x.append(e)
        d.append(x)

    print('\n[A] x [B] =')
    for i in range(row_a):
        for j in range(colm_b):
            print(d[i][j], end=" ")
        print()

menu = True

while menu is True:
    system('cls')
    print('\tMatrix Calculater by tejas')
    print('1. Addition of two matrices')
    print('2. Multiplication of two matrices')
    print('3. Both (rows and columns of two must same)')
    print('4. Exit')
    button = int(input('Enter choice : '))
    if button in range(1, 4):
        flag = 1
    elif button == 4:
        exit()
    else:
        print('Wrong input')
        exit()

    print('Enter matrices :')
    row_a = int(input('Enter rows of first matrix : '))
    colm_a = int(input('Enter columns of first matrix : '))
    row_b = int(input('\nEnter rows of second matrix : '))
    colm_b = int(input('Enter columns of second matrix : '))

    if button == 3:
        if row_a != row_b or colm_a != colm_b:
            print('Invalid Matrices for this choice')
            exit()

    print('Enter elements of matrix [A] : ')
    a = []
    for r in range(row_a):
        r = []
        for i in range(colm_a):
            r.append(int(input()))
        a.append(r)
    print(a)

    print('Enter elements of matrix [B] : ')
    b = []
    for r in range(row_b):
        r = []
        for i in range(colm_b):
            r.append(int(input()))
        b.append(r)
    print(b)
    
    if button is 1:
            MatAdd(a, b, row_a, colm_a, row_b, colm_b)
    if button is 2:
            MatMult(a, b, row_a, colm_a, row_b, colm_b)
    if button is 3:
            MatAdd(a, b, row_a, colm_a, row_b, colm_b)
            MatMult(a, b, row_a, colm_a, row_b, colm_b)
    ask = input('\n\nDo you want to continue ? y/n...')
    if ask == 'y':
        menu = True
    else:
        menu = False