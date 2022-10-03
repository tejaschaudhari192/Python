import random

num = random.randrange(1,100)
gameover=False

def compare(n):
    if n>num:
        return "too high"
    elif n<num:
        return "too low"
    elif n==num:
        return "Your guess is Right"
        gameover==True

diff=input("Choose Difficulty level\nEnter 0 for easy and 1 for hard : ")
if diff=="0":
    i=10
elif diff=="1":
    i=5
else:
    print("Wrong input")
    exit

while i>=1 or gameover:
    print(f"\nYou have {i} chances")
    n= int(input("Enter nuber : "))
    result= compare(n)
    print(result)
    
    if i==1:
        print("You are out of chance\n\nYou lose.....\n")
        print(f"Correct Guess was {num}")
        break
    elif result=="Your guess is Right":
        print("\nYou won")
        break

    i-=1