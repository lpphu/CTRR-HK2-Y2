# 52100988 Lữ Phúc Phú

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Get the public and private key in PEM format
public_key = key.publickey().export_key()
private_key = key.export_key()

# Create a cipher object using the public key
cipher = PKCS1_OAEP.new(RSA.import_key(public_key))

# Encrypt the message
message = b"Hello, World!"
ciphertext = cipher.encrypt(message)

# Print the encrypted message
print("Encrypted message: ", ciphertext)

# Create a cipher object using the private key
cipher = PKCS1_OAEP.new(RSA.import_key(private_key))

# Decrypt the message
plaintext = cipher.decrypt(ciphertext)

# Print the decrypted message
print("Decrypted message: ", plaintext.decode())