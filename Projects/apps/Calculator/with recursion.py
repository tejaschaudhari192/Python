logo = ''' 
 _____________________
|  _________________  |
| |  Teja's  Calci  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

functions = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calci():
    n1 = float(input("Enter first digit : "))

    for sign in functions:
        print(sign)

    repeat=True
    c=""
    while repeat:
        sign = input("Enter sign to perform operation : ")
        operation = functions[sign]
        n2 = float(input("Enter second digit : "))

        ans = operation(n1, n2)
        print(f"{n1} {sign} {n2} = {ans} ")
        n1=ans # for continue

        c=input("\n'y'for continue or 'n' for new operation or x to exit...")
        if c=="y":
            repeat=True
        elif c == 'x':
            exit()
        else:
            repeat=False
            calci()
# coded by tejas
calci()
