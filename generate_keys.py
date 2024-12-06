import os
from utils.rsa_keys import RSAKeys

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    print("Generating keys...")
    
    ensure_directory_exists('server/keys/')
    ensure_directory_exists('client/keys/')
    
    RSAKeys.generate_keys('server/keys/server_private_key.pem', 'server/keys/server_public_key.pem')
    RSAKeys.generate_keys('client/keys/client_private_key.pem', 'client/keys/client_public_key.pem')
    
    print("Keys generated successfully.")

if __name__ == "__main__":
    main()
