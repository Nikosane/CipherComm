import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from utils.secure_chat import SecureChat  
print("Secure Chat Server is running...")

import socket
from utils.secure_chat import SecureChat
from utils.rsa_keys import RSAKeys
from cryptography.hazmat.primitives import serialization 

HOST = '127.0.0.1'
PORT = 65432

def main():
    private_key = RSAKeys.load_private_key('server/keys/server_private_key.pem')
    public_key = RSAKeys.load_public_key('server/keys/server_public_key.pem')


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[INFO] Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"[INFO] Connected by {addr}")

            conn.send(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

            print("[INFO] Sent public key to client.")

            client_public_key_data = conn.recv(2048)
            client_public_key = RSAKeys.load_public_key_from_bytes(client_public_key_data)
            print("[INFO] Received client's public key.")
            secure_chat = SecureChat(private_key, client_public_key)

            while True:
                encrypted_message = conn.recv(2048)
                if not encrypted_message:
                    print("[INFO] Connection closed by client.")
                    break

                
                decrypted_message = secure_chat.decrypt_message(encrypted_message)
                print(f"Client: {decrypted_message}")

                
                response = input("You: ")
                encrypted_response = secure_chat.encrypt_message(response)
                conn.send(encrypted_response)

if __name__ == "__main__":
    main()
