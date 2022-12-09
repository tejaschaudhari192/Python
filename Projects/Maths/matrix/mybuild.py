from IPython.display import clear_output
from os import system

def MakeMatrix(rows, colms):
    Mat = []
    for r in range(rows):
        r = []
        for i in range(colms):
            r.append(int(input()))
        Mat.append(r)
    return Mat


def PrintMatrix(m, row_a, colm_a, row_b, colm_b):

    for i in m:
        print(i)
        # for j in range(colm_b):
        #     print(m[i][j], end="  ")
        # print()


def MatAddSub(A, B, row_a, colm_a, row_b, colm_b,op):
    '''Function to Add Matrix 
    arguments := rows and colums of both matrix'''
    c = []
    for i in range(row_a):
        r = []
        for j in range(colm_a):
            if op is 1:
                r.append(A[i][j]+B[i][j])
            else:
                r.append(A[i][j]-B[i][j])
        c.append(r)

    print('\n[A] + [B] =\n')
    PrintMatrix(c, row_a, colm_a, row_b, colm_b)


def MatMult(A, B, row_a, colm_a, row_b, colm_b):
    '''Function to multiply Matrix 
    arguments := rows and colums of both matrix'''
    d = []
    for c in range(row_a):
        x = []
        for r in range(colm_b):
            e = 0
            for k in range(colm_a):
                e += A[c][k]*B[k][r]
            x.append(e)
        d.append(x)

    print('\n[A] x [B] =\n')
    PrintMatrix(d, row_a, colm_a, row_b, colm_b)


menu = True

while menu is True:
    system('cls')
    clear_output()
    flag = 0
    print('Enter matrices :')
    # Matrix [A]
    print(f'Enter Dimentions of matrix [A] : ')
    row_a = int(input('Enter rows of first matrix : '))
    colm_a = int(input('Enter columns of first matrix : '))
    print('Enter elements : ')
    A = MakeMatrix(row_a, colm_a)
    print('\n[A] =')
    for i in A:
        print(i)
    # Matrix [B]
    print('\nEnter elements of matrix [B] : ')
    row_b = int(input('Enter rows of second matrix : '))
    colm_b = int(input('Enter columns of second matrix : '))
    print('Enter elements : ')
    B = MakeMatrix(row_b, colm_b)
    print('\n[B] =')
    for i in B:
        print(i)
        
    press = input('Enter any key to continue...')
    back = False
    while back is False:
        system('cls')
        clear_output()
        print('\n\tMatrix operations')
        print('\n1. Addition of two matrices')
        print('2. Subtraction of two matrices')
        print('3. Multiplication of two matrices')
        print('4. Exit')
        button = int(input('Enter choice : '))
        if button not in range(1, 5):
            print('Wrong input')
            flag = 1

        # Dimentions check
        if button is 1 or button is 2:
            if row_a is not row_b or colm_a is not colm_b:
                print('\n\tDimention Error !!')
                flag = 2
        elif button is 3:
            if row_a is not colm_b:
                print('\n\tDimention Error !!')
                flag = 2
        
        # Operations
        if flag is not 2:
            if button is 1:
                MatAddSub(A, B, row_a, colm_a, row_b, colm_b,1)
            elif button is 2:
                MatAddSub(A, B, row_a, colm_a, row_b, colm_b,2)
            elif button is 3:
                MatMult(A, B, row_a, colm_a, row_b, colm_b)
            elif button is 4:
                exit()
        askb = input('\n\nPerform another operation on same matrices ? y/n...')
        if askb is 'y':
            back = False
        else:
            back = True
            

    ask = input('\n\nEnter new matrices ? y/n...')
    if ask is 'y':
        menu = True
    else:
        menu = False


system('cls')
clear_output()
print('\n\nExiting the Program .....')