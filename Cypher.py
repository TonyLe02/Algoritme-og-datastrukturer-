def vigenere_decipher(ciphertext, keyword):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Initialize the plaintext
    plaintext = ''
    
    # Initialize the keyword index
    keyword_index = 0
    
    # Iterate over each character in the ciphertext
    for char in ciphertext:
        # If the character is a letter
        if char.isalpha():
            # Calculate the shift value
            shift = alphabet.index(keyword[keyword_index % len(keyword)])
            
            # Decipher the character
            plaintext += alphabet[(alphabet.index(char) - shift) % len(alphabet)]
            
            # Increment the keyword index
            keyword_index += 1
        else:
            # If the character is not a letter, add it to the plaintext as is
            plaintext += char
    
    # Return the plaintext
    return plaintext

# Define the ciphertext and the keyword
ciphertext = 'dhzdqq qcc'
keyword = 'dog'

# Decipher the ciphertext and print the plaintext
print(vigenere_decipher(ciphertext, keyword))
