bill = input("Enter bill : ")
tip=input("tip : ")
f = input("How many friends : ")

ctip = float(bill) * (float(tip)/100)
total=int(tip)+float(bill)
print(f"Tip per person is {round((total/int(f)),2)} ")
