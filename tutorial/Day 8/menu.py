#   13-09-2022
#   6:00 pm

def encode(text):
    word=""
    encoded=""
    for letter in text:
        word=letter
        positn=alphabet.index(word)

        shiftnum = positn+shift
        if shiftnum>25:
            shiftnum=shiftnum-25

        encoded+= alphabet[shiftnum]

    print(f"Encrypted messege is {encoded}")

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

choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message : ").lower()
shift = int(input("Type the shift number : "))

if choice=="encode":
    encode(text)
elif choice=="decode":
    decode(text)
else:
    print("Choose correct choice....")

# coded by tejas

print("\n\n....₵◉Đ€▷    ₿ ¥    †é✓△$   ^_~")
print("Visit repobytejas.blogspot.com for more\n\n")

