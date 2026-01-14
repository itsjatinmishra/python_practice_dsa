# XOR Encryption and Decryption

# Original data
data = 15
key = 7

# Encrypt the data
encrypted = data ^ key
print("Encrypted:", encrypted)

# Decrypt the data
decrypted = encrypted ^ key
print("Decrypted:", decrypted)