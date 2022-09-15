def encode(text):
    word = ""
    encoded = ""
    for letter in text:
        word = letter
        positn = alphabet.index(word)

        shiftnum = positn+shift
        if shiftnum > 25:
            shiftnum = shiftnum-25

        encoded += alphabet[shiftnum]

    print(f"Encrypted messege is {encoded}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encode(text)
