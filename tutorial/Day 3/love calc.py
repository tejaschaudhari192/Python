print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1 + name2
lname = name.lower()

n1 = 0
r = 0

r = lname.count("t")
n1 += r
r = lname.count("r")
n1 += r
r = lname.count("u")
n1 += r
r = lname.count("e")
n1 += r
true = n1
print(true)

n1 = 0
r = lname.count("l")
n1 += r
r = lname.count("o")
n1 += r
r = lname.count("v")
n1 += r
r = lname.count("e")
n1 += r
love = n1
print(love)

tl = str(true)+str(love)

score = int(tl)

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
