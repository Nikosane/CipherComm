from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class SecureChat:
    def __init__(self, private_key, peer_public_key):
        self.private_key = private_key
        self.peer_public_key = peer_public_key

    def encrypt_message(self, message):
        return self.peer_public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decrypt_message(self, encrypted_message):
        return self.private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()
