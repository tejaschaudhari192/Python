class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Not equal"



print(2 < 3)

print("\nwith Operator overloading :")
ob1 = A(4)
ob2 = A(2)
print(ob1 < ob2)
print()
ob3 = A(2)
ob4 = A(3)
print(ob3 == ob4)
