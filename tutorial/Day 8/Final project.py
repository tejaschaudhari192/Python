def coding(text,choice,shift):
    word=""
    coded=""
    if choice=="encode":
        shift *=-1

    for char in text:
        if char in alphabet:
            positn=alphabet.index(char)
            shiftnum = positn-shift
            coded+= alphabet[shiftnum]
        else:
            coded+=char

    print(f"{choice}d messege is {coded}")
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat=True
while repeat:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt : ")
    text = input("Type your message : ").lower()
    shift = int(input("Type the shift number : "))
    shift=shift%26
    coding(text,choice,shift)

    repeat=input("Do you want to repeat ? y/n... ")
    if repeat=="y":
        repeat=True
    else:
        repeat=False