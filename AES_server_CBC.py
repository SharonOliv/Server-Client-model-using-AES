import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b"#@TOPSECRETKEY!!" 

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode() 

def decrypt(ciphertext_b64, key):
    try:
        ciphertext = base64.b64decode(ciphertext_b64) 
        iv = ciphertext[:AES.block_size]
        encrypted_message = ciphertext[AES.block_size:]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(encrypted_message), AES.block_size)
        return plaintext.decode()

    except ValueError:
        print("Decryption error!")
        return None

def main():
    server_ip = "10.1.95.93"
    server_port = 21312

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print(f"Server started on {server_ip}:{server_port}. Waiting for connections...")

    try:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        while True:
            encrypted_message = conn.recv(1024).decode()
            if not encrypted_message or encrypted_message.lower() == "bye":
                print("Client disconnected.")
                break

            print(f"CLIENT SENT (encrypted, BASE64): {encrypted_message}")

            decrypted_message = decrypt(encrypted_message, key)
            if decrypted_message:
                print(f"CLIENT SENT (decrypted): {decrypted_message}")

            server_message = input("SERVER (plaintext): ")

            encrypted_response = encrypt(server_message, key)

            print(f"SERVER SENDING (plaintext): {server_message}")
            print(f"SERVER SENDING (encrypted, BASE64): {encrypted_response}")

            conn.send(encrypted_response.encode())

            if server_message.lower() == "bye":
                print("Closing connection...")
                break

    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        conn.close()
        server_socket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    main()