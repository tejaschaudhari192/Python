arr = [1,2,3,4,5]
def fun1(x):
    return (x+1)
def fun2(x):
    return (x%2 == 0)
sol = map(fun1,arr)
sol = filter(fun2,arr)
print(list(sol))