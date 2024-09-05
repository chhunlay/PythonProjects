alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get user inputs for direction, text, and shift amount
direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Define the encryption function
def caesar_cipher(original_text, shift_amount, cipher_direction):
    cipher_text = ""
    
    # Adjust the shift direction based on encoding or decoding
    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            # Find the new position and wrap around using modulus
            shifted_position = (alphabet.index(letter) + shift_amount) % 26
            cipher_text += alphabet[shifted_position]
        else:
            # Add the letter as it is if it's not in the alphabet
            cipher_text += letter
        
    print(f"Here is the {cipher_direction}d result: {cipher_text}")
    
# Call the function based on the user input direction
caesar_cipher(original_text=text, shift_amount=shift, cipher_direction=direction)
