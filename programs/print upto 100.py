def printf(n):
    if n is 101:
        return
    print(n)
    printf(n+1)

printf(1)
