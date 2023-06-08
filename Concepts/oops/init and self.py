class animal():
    def __init__(self, a,b):
        self.math = a
        self.geo = b

obj = animal(a=97,b=70)#arg (self) -> (obj)
print(obj.math)


class A():
    def __init__(self, count = None):
        self.count = count

'''
a1 = A()
a2 = A(102)
print(a1.count)
print(a2.count)
'''
class test():
    def __init__(self):
        self.x = 0
class ok(test):
    def __init__(self):
        test.__init__(self)
        self.y = 0  
def main():  
    b = ok()
    print(b.x,b.y)
main()
    # '''

key = 100
try:
    key = key/0
except ZeroDivisionError:
    print('hacked',end='')
else:
    print('runned',end='')
finally:
    print('done',end='')
    