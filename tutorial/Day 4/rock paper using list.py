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
choice = [rock,paper,scissor]
p = int(input("enter 1 for rock, 2 for paper & 3 for Scissor to choose"))

c = random.randint(1,3)

if p>3 or p<1:
    print("enter valid input...")
else :
    print("You :")
    print(choice[p-1]) #-1 bcoz index value stars from 0
    print("Computer :")
    print(choice[c-1])

    if c == p:
        print("tie")
    elif p == 1 and c == 3:
        print("You win")
    elif p == 2 and c == 1:
        print("You win")
    elif p == 3 and c == 2:
        print("You win")
    else:
        print("You lose")

