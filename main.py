"""SecureVault Lite: beginner-friendly file encryption project."""
from pathlib import Path
import base64
import hashlib
import secrets
from cryptography.fernet import Fernet, InvalidToken

MAGIC = b"SVLT"
SALT_LENGTH = 16


def make_key(password, salt):
    """Convert a password into an encryption key."""
    password_bytes = password.encode("utf-8")
    key_bytes = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, 200_000, dklen=32)
    return base64.urlsafe_b64encode(key_bytes)


def encrypt_file():
    file_name = input("Enter the file path to encrypt: ").strip('"')
    password = input("Create a password: ")

    if not password:
        print("Password cannot be empty.")
        return

    file_path = Path(file_name)
    if not file_path.is_file():
        print("File not found. Check the path and try again.")
        return

    try:
        file_data = file_path.read_bytes()
        salt = secrets.token_bytes(SALT_LENGTH)
        key = make_key(password, salt)
        encrypted_data = Fernet(key).encrypt(file_data)

        output_path = Path(str(file_path) + ".enc")
        output_path.write_bytes(MAGIC + salt + encrypted_data)

        print("Encryption successful!")
        print("Encrypted file:", output_path)
        print("Original file has not been deleted.")
    except OSError as error:
        print("File error:", error)


def decrypt_file():
    file_name = input("Enter the encrypted file path: ").strip('"')
    password = input("Enter the password: ")

    file_path = Path(file_name)
    if not file_path.is_file():
        print("File not found. Check the path and try again.")
        return

    try:
        encrypted_file = file_path.read_bytes()

        if not encrypted_file.startswith(MAGIC) or len(encrypted_file) < 20:
            print("This is not a valid SecureVault Lite file.")
            return

        salt = encrypted_file[4:20]
        encrypted_data = encrypted_file[20:]
        key = make_key(password, salt)

        try:
            original_data = Fernet(key).decrypt(encrypted_data)
        except InvalidToken:
            print("Wrong password or encrypted file is damaged.")
            return

        if file_path.name.endswith(".enc"):
            output_name = file_path.name[:-4]
        else:
            output_name = file_path.name + ".restored"

        output_path = file_path.with_name("restored_" + output_name)
        output_path.write_bytes(original_data)

        print("Decryption successful!")
        print("Restored file:", output_path)
    except OSError as error:
        print("File error:", error)


def main():
    while True:
        print("\n========== SecureVault Lite ==========")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            encrypt_file()
        elif choice == "2":
            decrypt_file()
        elif choice == "3":
            print("Thank you for using SecureVault Lite.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
