
def decode(text):
    word=""
    decoded=""
    for letter in text:
        word=letter
        positn=alphabet.index(word)

        shiftnum = positn-shift
        if shiftnum<0:
            shiftnum=shiftnum+25

        decoded+= alphabet[shiftnum]

    print(f"Decrypted messege is {decoded}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

decode(text)

