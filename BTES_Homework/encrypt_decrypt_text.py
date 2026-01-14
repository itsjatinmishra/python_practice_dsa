# XOR encryption and decryption for text

def text_xor_encrypt_decrypt(text, key):
    result = ""
    for char in text:
        # XOR each character's ASCII code with the key
        result += chr(ord(char) ^ key)
    return result

# Original text
original_text = "HELLO"
key = 5

# Encrypt
encrypted_text = text_xor_encrypt_decrypt(original_text, key)
print("Encrypted Text:", encrypted_text)

# Decrypt
decrypted_text = text_xor_encrypt_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)