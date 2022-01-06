
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text_input = "haha hehe hihi 3"
text = text_input.split(" ")
x = 0
shift_input = 5
text_encrypted = []

chipper = ""
caesar = []
x = 0
for letter in text_input:
    # print(text_input[x])
    if letter in alphabet:
        chiper = alphabet.index(letter)
        encrypt = chiper + shift_input
        if encrypt > 26:
            encrypt %= 26
        chipper += alphabet[encrypt]
    else : 
        chipper += letter
    # print(text_encrypted)
print(chipper)
# chipper = ''.join(text_encrypted)
