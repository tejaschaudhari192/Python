# 16-09-22
# 
def upto_n():
    ep = int(input("Enter ending point : "))
    n = 1
    while n <= ep:
        i = 2
        flag = 0
        while i < n:
            if n % i == 0:
                flag = 1
            i += 1
        if flag == 0:
            print(n)

        n += 1


def nth_term():
    ep = int(input("Enter nth term: "))
    n = 1
    count = 1
    while count <= ep:
        i = 2
        flag = 0
        while i < n:
            if n % i == 0:
                flag = 1
            i += 1
        if flag == 0:
            print(n)
            count += 1

        n += 1


c = int(input("Enter 1 for upto n terms or 2 for first n terms :"))

if c == 1:
    upto_n()
else:
    nth_term()

# coded by twjas
