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