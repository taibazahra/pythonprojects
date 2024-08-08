direction = input("type encode to encrypt and decode to decrypt: " )
if direction == 'encode':
    alphabet= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    plain_text = input("Type you message: ").upper()
    shift = int(input("type the shift value: ")) 
    def encrypt(text,shift_amt):
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position+shift
            new_letter = alphabet[new_position]
            cipher_text+=new_letter
        print(cipher_text)
    encrypt(text = plain_text, shift_amt = shift)
elif direction=='decode':
    alphabet= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cipher_text = input("Type you message: ").upper()
    shift = int(input("type the shift value: ")) 
    def decrypt(text,shift_amt):
        decrypt_text = ""
        for letters in text:
            positions = alphabet.index(letters)
            new_positions = positions-shift
            new_letters = alphabet[new_positions]
            decrypt_text+=new_letters 
        print(decrypt_text)
    decrypt(text = cipher_text, shift_amt = shift  )
