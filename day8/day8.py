alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text_input, shift_input, direction_input):

    chipper = ""
    x = 0
    for letter in text_input:
        if letter in alphabet:
            chiper = alphabet.index(letter)
            if direction_input == "encode":
                encrypt = chiper + shift_input
            elif direction_input == "decode":
                encrypt = chiper - shift_input
            if encrypt > 26:
                encrypt %= 26
            chipper += alphabet[encrypt]
        else : 
            chipper += letter
    print(chipper)

run = True

while run == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    run_again = input("Do You wanna run this program again? type 'yes' or 'no' ")
    if run_again == "no":
        run = False





