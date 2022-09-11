import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

p = input("\n\nEnter R,P,S to choose :\n").lower()

print("You :")
if p == "r":
    print(rock)
elif p == "p":
    print(paper)
elif p == "s":
    print(scissor)
else:
    print("enter valid input...")
    exit()

c = random.choice(["r", "p", "s"])
print("Computer :")

if c == "r":
    print(rock)
elif c == "p":
    print(paper)
elif c == "s":
    print(scissor)
else:
    print("enter valid input...")

if c == p:
    print("tie")
elif p == "r" and c == "s":
    print("You win")
elif p == "s" and c == "p":
    print("You win")
elif p == "p" and c == "r":
    print("You win")
else:
    print("You lose")
