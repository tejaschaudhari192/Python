import os
import random
game_over=True


chosen_word ="chaudhari"

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


#creating blank list
wordlist=[]
for char in chosen_word:
    wordlist+="-"

j=0

logo=''' 
                                                                              
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,    
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88 
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88 
                                    aa,    ,88                                
                                     "Y8bbdP"                         '''

print(f"{logo}-----Made by Tejas ")
print("\n\n\n\nYoy Have 6 Lives to play this game")
print("Guess the correct letter in word to win the game")


hanger=['''
  +---+
  |   |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

win=False
i=0
while i<=6:
    print(hanger[i])
    guess = input("Guess a letter: ").lower()
    k=0
    for char in range(len(wordlist)):
        if chosen_word[char]== guess:
            wordlist[char]=" "+guess
            k+=1

    if k==0:
      print(f"\nWrong guess Remaining Lives {6-i}")
      i+=1
    else:
      print("\nCorrect Guess")
    
    display=""

    for char in wordlist:
      display+=char

    print(display)
    j+=1

    if "-" not in wordlist:
        win = True
        i=10

if win:
    print("Won beti")
else:
    print("Lose Bacchi")