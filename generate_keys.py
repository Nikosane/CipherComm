from utils.rsa_keys import RSAKeys

def main():
    print("Generating keys...")
    RSAKeys.generate_keys('server/keys/server_private_key.pem', 'server/keys/server_public_key.pem')
    RSAKeys.generate_keys('client/keys/client_private_key.pem', 'client/keys/client_public_key.pem')
    print("Keys generated successfully.")

if __name__ == "__main__":
    main()
