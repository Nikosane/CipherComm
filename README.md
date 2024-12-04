# CipherComm

This repository contains a secure chat application with end-to-end encryption using RSA keys.

## Features
- Secure communication with RSA-based encryption.
- Separate client and server modules.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Generate RSA keys:
   - Run `utils/rsa_keys.py` to generate keys for both server and client.

3. Start the server:
   ```bash
   python server/server.py
   ```

4. Start the client:
   ```bash
   python client/client.py
   ```
