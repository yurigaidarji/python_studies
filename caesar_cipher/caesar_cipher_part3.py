
# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decrypted_text += letter
        else:
            shifted_position = alphabet.index(letter) - shift_amount
            decrypted_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {decrypted_text}")

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

def caesar(direction, text, shift):
    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    else:
        decrypt(original_text=text, shift_amount=shift)


should_continue = True
while should_continue: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    
    continue_prog = input("Do you want to continue? [Y/N]")
    if continue_prog == "N" or continue_prog == "n":
        should_continue = False

