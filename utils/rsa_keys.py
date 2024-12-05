from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

class RSAKeys:
    @staticmethod
    def generate_keys(private_key_path, public_key_path):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        
        with open(private_key_path, 'wb') as private_file:
            private_file.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        
        with open(public_key_path, 'wb') as public_file:
            public_file.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

    @staticmethod
    def load_private_key(file_path):
        with open(file_path, 'rb') as key_file:
            return load_pem_private_key(key_file.read(), password=None)

    @staticmethod
    def load_public_key(file_path):
        with open(file_path, 'rb') as key_file:
            return load_pem_public_key(key_file.read())

    @staticmethod
    def load_public_key_from_bytes(key_data):
        return load_pem_public_key(key_data)
