a=0
b=1
c=0

op=int(input("Enter 1 for print upto n or 2 for first n terms : "))

if op==1:
    num=int(input("Fibpnacci upto : "))

    while c<=num:
        print(c)
        a=b
        b=c
        c=a+b
else:
    num=int(input("nth term of fibonacci series : "))
    i=1
    while i<=num:
        print(c)
        a=b
        b=c
        c=a+b
        i+=1
