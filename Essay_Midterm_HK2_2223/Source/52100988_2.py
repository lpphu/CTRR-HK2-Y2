# 52100988 Lữ Phúc Phú

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate RSA key pair
def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Encrypt a message with RSA public key
def encrypt_message(message, public_key):
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# Decrypt a message with RSA private key
def decrypt_message(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()
