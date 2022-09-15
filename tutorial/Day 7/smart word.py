
import random

words = ["antariksh", "bhavsar", "chaudhari"]

word = random.choice(words)

c = input("Enter char : ")

for char in word:
    if c == char:
        print("yes")
    else:
        print("no")
