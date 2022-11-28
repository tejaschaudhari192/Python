from os import system

def PrintMatrix(m, row_a, colm_a, row_b, colm_b):
    
    for i in range(row_a):
        for j in range(colm_b):
            print(m[i][j], end=" ")
        print()
    
def MatAdd(a, b, row_a, colm_a, row_b, colm_b):
    '''Function to Add Matrix 
    arguments := rows and colums of both matrix'''
    if row_a != row_b or colm_a != colm_b:
        print('Dimention Error !!!');
        exit();
    c = []
    for i in range(row_a):
        r = []
        for j in range(colm_a):
            r.append(a[i][j]+b[i][j])
        c.append(r)
        
    print('\n[A] + [B] =')
    PrintMatrix(c, row_a, colm_a, row_b, colm_b)

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
    PrintMatrix(d, row_a, colm_a, row_b, colm_b)

menu = True

while menu is True:
    
    system('cls')
    flag =0;
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

    # Dimentions check
    if button is 3 or button is 1:
        if row_a is not row_b or colm_a is not colm_b:
            print('Dimention Error !!')
            flag = 2
    elif button is 2:
        if row_a is not colm_b :
            print('Dimention Error !!')
            flag = 2
            
        
    if flag is not 2:  
        # Matrix [A]
        print('Enter elements of matrix [A] : ')
        a = []
        for r in range(row_a):
            r = []
            for i in range(colm_a):
                r.append(int(input()))
            a.append(r)
        print('\n[A] =',a)

        # Matrix [B]
        print('Enter elements of matrix [B] : ')
        b = []
        for r in range(row_b):
            r = []
            for i in range(colm_b):
                r.append(int(input()))
            b.append(r)
        print('\n[B] =',b)
        
        if button is 1:
                MatAdd(a, b, row_a, colm_a, row_b, colm_b)
        elif button is 2:
                MatMult(a, b, row_a, colm_a, row_b, colm_b)
        elif button is 3:
                MatAdd(a, b, row_a, colm_a, row_b, colm_b)
                MatMult(a, b, row_a, colm_a, row_b, colm_b)
        elif button is 4:
            exit()
                
    ask = input('\n\nDo you want to continue ? y/n...')
    if ask is 'y':
        menu = True
    else:
        menu = False