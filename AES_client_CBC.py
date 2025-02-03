import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b"#@TOPSECRETKEY!!"

def encrypt(plaintext, key):
    cipher=AES.new(key, AES.MODE_CBC)
    ciphertext=cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode()  # Encode IV + Ciphertext in Base64

def decrypt(ciphertext_b64, key):
    try:
        ciphertext=base64.b64decode(ciphertext_b64)  # Decode Base64
        iv=ciphertext[:AES.block_size]  # Extract IV
        encrypted_message=ciphertext[AES.block_size:]  # Extract encrypted data

        cipher=AES.new(key, AES.MODE_CBC, iv)
        plaintext=unpad(cipher.decrypt(encrypted_message), AES.block_size)
        return plaintext.decode()

    except ValueError:
        print("Decryption error!")
        return None

def main():
    server_ip="10.1.95.93" 
    server_port=21312

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    print(f"Connected to server at {server_ip}:{server_port}")

    try:
        while True:
            client_message = input("CLIENT (plaintext): ")
            encrypted_message = encrypt(client_message, key)

            print(f"CLIENT SENDING (plaintext): {client_message}")
            print(f"CLIENT SENDING (encrypted, BASE64): {encrypted_message}")

            client_socket.send(encrypted_message.encode())

            if client_message.lower() == "bye":
                print("Disconnecting from server...")
                break

            encrypted_response = client_socket.recv(1024).decode()
            print(f"SERVER SENT (encrypted, BASE64): {encrypted_response}")

            decrypted_response = decrypt(encrypted_response, key)
            if decrypted_response:
                print(f"SERVER SENT (decrypted): {decrypted_response}")

    except KeyboardInterrupt:
        print("\nClient shutting down.")
    finally:
        client_socket.close()
        print("Client socket closed.")

if __name__ == "__main__":
    main()