import os
import uuid
import base64
import struct
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(password: str) -> bytes:
    """Derives a secure cryptographic Fernet key from any text password."""
    salt = b'static_salt_for_folder_encryption' 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_folder(folder_path, key):
    """Encrypts all files, embedding the original filename inside the encrypted data."""
    f = Fernet(key)
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            original_path = os.path.join(root, file)
            
            stat_info = os.stat(original_path)
            original_atime = stat_info.st_atime
            original_mtime = stat_info.st_mtime

            # Generate a random name to mask user data
            ext = os.path.splitext(file)[1]
            new_filename = str(uuid.uuid4()) + ext
            new_path = os.path.join(root, new_filename)

            try:
                with open(original_path, "rb") as file_in:
                    file_data = file_in.read()
                
                filename_bytes = file.encode('utf-8')
                filename_len = len(filename_bytes)
                
                payload = struct.pack("!H", filename_len) + filename_bytes + file_data
                encrypted_data = f.encrypt(payload)

                with open(new_path, "wb") as file_out:
                    file_out.write(encrypted_data)

                os.utime(new_path, (original_atime, original_mtime))
                os.remove(original_path)
                
                print(f"Encrypted and Hidden: {file} -> {new_filename}")
            except Exception as e:
                print(f"Failed to encrypt {file}: {e}")

    print("Encryption complete.")

def decrypt_folder(folder_path, key):
    """Decrypts files and extracts the original names from the payload."""
    f = Fernet(key)
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            encrypted_path = os.path.join(root, file)

            stat_info = os.stat(encrypted_path)
            saved_atime = stat_info.st_atime
            saved_mtime = stat_info.st_mtime

            try:
                with open(encrypted_path, "rb") as file_in:
                    encrypted_data = file_in.read()
                
                decrypted_payload = f.decrypt(encrypted_data)
                
                filename_len = struct.unpack("!H", decrypted_payload[:2])[0]
                
                original_filename = decrypted_payload[2:2+filename_len].decode('utf-8')
                file_data = decrypted_payload[2+filename_len:]
                
                original_path = os.path.join(root, original_filename)

                with open(original_path, "wb") as file_out:
                    file_out.write(file_data)

                os.utime(original_path, (saved_atime, saved_mtime))
                os.remove(encrypted_path)
                
                print(f"Decrypted: {file} -> {original_filename}")
            except Exception as e:
                print(f"Skipping {file}: Could not decrypt or not a valid payload.")

    print("Decryption complete.")

if __name__ == "__main__":
    # 1. ASK FOR THE OPERATION FIRST
    print("1. Encrypt Folder\n2. Decrypt Folder")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice not in ["1", "2"]:
        print("Error: Invalid choice. Exiting.")
    else:
        # 2. ASK FOR THE PATH AND PASSWORD AFTERWARD
        target_folder = input("Enter the full path to the folder: ").strip()

        if not os.path.exists(target_folder) or not os.path.isdir(target_folder):
            print("Error: The specified folder path does not exist.")
        else:
            user_password = input("Enter your custom text key/password: ").strip()
            if not user_password:
                print("Error: Key cannot be empty.")
            else:
                crypto_key = derive_key(user_password)
                
                if choice == "1":
                    encrypt_folder(target_folder, crypto_key)
                elif choice == "2":
                    decrypt_folder(target_folder, crypto_key)
