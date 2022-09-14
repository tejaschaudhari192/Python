

chosen_word ="chaudhari"

#Testing code
print(f'Pssst, the solution is {chosen_word}.')



wordlist=[]


for char in chosen_word:
    wordlist+='_'




j=0
while game_over :

    guess = input("Guess a letter: ").lower()

    for char in range(len(wordlist)):
        if chosen_word[char]== guess:
            wordlist[char]=guess

    print(wordlist)
    j+=1

    if "_" not in wordlist:
        game_over=False

print(j)