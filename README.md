# Server-Client Model using AES Encryption
This repository contains the implementation of **AES (Advanced Encryption Standard)** encryption and decryption in a **client-server model**, enabling secure **dual communication** between the server and client.

Both **CBC (Cipher Block Chaining)** and **ECB (Electronic Codebook)** modes of AES are implemented for message exchange.

## Overview

This repo demonstrates:
- Secure communication between a client and server using **AES encryption**.
- Encryption and decryption of messages using both **CBC** and **ECB** modes.
- Real-time dual communication where both client and server can send and receive encrypted messages.

**AES** is a widely used symmetric encryption algorithm known for its high performance and security.

## Features

- Encrypt outgoing messages using AES (CBC and ECB modes).
- Decrypt incoming messages securely.
- Enable two-way (dual) encrypted communication between server and client.
- Different AES modes allow learning the difference between **block chaining** and **independent block encryption**.

## Technologies Used

- Python 3
- `pycryptodome` library (`Crypto.Cipher.AES`)
- Socket programming (TCP sockets)

## How to Run

1. Install dependencies:
   ```bash
   pip install pycryptodome
   ```

2. To run with **CBC mode**:
   - Start the server:
     ```bash
     python AES_server_CBC.py
     ```
   - In another terminal, start the client:
     ```bash
     python AES_client_CBC.py
     ```

3. To run with **ECB mode**:
   - Start the server:
     ```bash
     python AES_server_ECB.py
     ```
   - In another terminal, start the client:
     ```bash
     python AES_client_ECB.py
     ```

4. Begin secure communication between the server and client!

## File Structure

| File Name           | Description                                   |
|---------------------|-----------------------------------------------|
| AES_client_CBC.py    | Client implementation using AES in CBC mode   |
| AES_client_ECB.py    | Client implementation using AES in ECB mode   |
| AES_server_CBC.py    | Server implementation using AES in CBC mode   |
| AES_server_ECB.py    | Server implementation using AES in ECB mode   |

## Notes

- **CBC Mode**: Each block of plaintext is XORed with the previous ciphertext block before being encrypted. Requires an IV (Initialization Vector).
- **ECB Mode**: Each block of plaintext is encrypted independently. Faster but less secure than CBC mode.
- This repo is intended for educational purposes to demonstrate secure client-server communication using AES.
