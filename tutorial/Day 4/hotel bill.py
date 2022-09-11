import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(len(names))
print(names[2])

payer = random.randint(1,4)

if payer==1:
    print(names[0],"is going to buy the meal today!")
elif payer==2:
    print(names[1],"is going to buy the meal today!")
elif payer==3:
    print(names[2],"is going to buy the meal today!")
else :
    print(names[3],"is going to buy the meal today!")