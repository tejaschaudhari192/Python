def add(a=None, b=None, c=None):
    if c == None:
        return a + b
    else:
        return a + b + c


print(f"Sum is {add(1, 2, 3)}")
