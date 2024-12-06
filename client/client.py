import socket
from utils.secure_chat import SecureChat
from utils.rsa_keys import RSAKeys
from cryptography.hazmat.primitives import serialization

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

def main():
    private_key = RSAKeys.load_private_key('client/keys/client_private_key.pem')
    public_key = RSAKeys.load_public_key('client/keys/client_public_key.pem')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            print(f"[INFO] Connected to server {SERVER_HOST}:{SERVER_PORT}")

            # Receive the server's public key
            server_public_key_data = client_socket.recv(2048)
            if not server_public_key_data:
                print("[ERROR] Failed to receive server public key.")
                return
            
            server_public_key = RSAKeys.load_public_key_from_bytes(server_public_key_data)
            print("[INFO] Received server's public key.")

            # Send the client's public key to the server
            client_socket.send(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )
            print("[INFO] Sent public key to server.")

            secure_chat = SecureChat(private_key, server_public_key)

            while True:
                # Send encrypted messages
                message = input("You: ")
                encrypted_message = secure_chat.encrypt_message(message)
                client_socket.send(encrypted_message)

                # Receive and decrypt the server's response
                encrypted_response = client_socket.recv(2048)
                if not encrypted_response:
                    print("[INFO] Connection closed by server.")
                    break

                decrypted_response = secure_chat.decrypt_message(encrypted_response)
                print(f"Server: {decrypted_response}")

        except Exception as e:
            print(f"[ERROR] Error occurred: {e}")

if __name__ == "__main__":
    main()
