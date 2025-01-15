import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
want = True
while want:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caser(original_text,shift_amount,directions):
        if directions == "encode":
            encrypt(original_text=original_text,shift_amount=shift_amount)
        elif directions == "decode":
            decrypt(original_text=original_text,shift_amount=shift_amount)
    def encrypt(original_text,shift_amount):
        encoded = ""
        for letter in original_text:
            a = alphabet.index(letter) + shift_amount
            if a>26:
                a = a-26
                encoded+=alphabet[a]
            else:
                encoded+=alphabet[a]
        print(encoded)
    def decrypt(original_text,shift_amount):
        encoded = ""
        for letter in original_text:
            a = alphabet.index(letter) - shift_amount
            if a<0:
                a = a+26
                encoded+=alphabet[a]
            else:
                encoded+=alphabet[a]
        print(encoded)
    caser(original_text=text,shift_amount=shift,directions=direction)
    a = input("Do you want to continue? Enter yes or no.").lower()
    if a == "no":
        want = False
