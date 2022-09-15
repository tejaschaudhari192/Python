y = int(input("Enter year"))
if y % 100 == 0:
    print("n")
elif y % 4 == 0:
    print("y")
elif y % 400 == 0:
    print("y")
else:
    print("n")
