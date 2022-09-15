# Step 2


chosen_word = "chaudhari"

# Testing code
print(f'Pssst, the solution is {chosen_word}.')


wordlist = []


for char in chosen_word:
    wordlist += '_'


game_over = True

i = 0
while game_over:

    guess = input("Guess a letter: ").lower()

    for char in range(len(wordlist)):
        if chosen_word[char] == guess:
            wordlist[char] = guess

    print(wordlist)
    i += 1

    if "_" not in wordlist:
        game_over = False

print(i)
