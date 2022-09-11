import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("For Generating an random password !")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

for let in range(1,int(nr_symbols)+1):
    rlet = random.randint(0,len(letters)-1)
    password.append(letters[rlet])

for sym in range(1,int(nr_symbols)+1):
    rsym = random.randint(0,len(symbols)-1)
    password.append(symbols[rsym])

for num in range(1,int(nr_numbers)+1):
    rnum = random.randint(0,len(numbers)-1)
    password.append(numbers[rnum])

print(f"Youe password is {password}\n\n")   #non random list

random.shuffle(password)    #random list


rampass=""

for char in password:
    rampass+=char

print(f"Youe password is {rampass}")   #random order

print("\n\n....₵◉Đ€▷    ₿ ¥    †é✓△$   ^_~")
print("Visit repobytejas.blogspot.com for more")