# SecureVault Lite — Python Project

## 1. Introduction
SecureVault Lite is a simple Python application that encrypts and decrypts files using a password. It is designed as a beginner-friendly demonstration of file handling and basic cybersecurity concepts.

## 2. Problem Statement
Files may contain private or important information. If someone accesses a file without permission, its contents may be exposed. SecureVault Lite encrypts a file so that it cannot be read normally and restores it when the correct password is provided.

## 3. Objectives
- Learn Python functions and menu-driven programming.
- Read and write files.
- Encrypt and decrypt file contents.
- Use password-based key derivation.
- Handle wrong passwords and file errors.

## 4. Features
1. Encrypt a file.
2. Decrypt an encrypted file.
3. Exit the program.
4. Preserve the original file.
5. Detect wrong passwords or damaged encrypted data.

## 5. Tools Used
- Python
- `cryptography` library
- Visual Studio Code

## 6. Working
The user selects an option from the menu. For encryption, the program reads the selected file, creates a random salt, derives an encryption key from the password, encrypts the file, and saves it with the `.enc` extension. For decryption, the program reads the salt from the encrypted file, derives the same key from the password, and restores the original content.

## 7. Algorithm
1. Start the program.
2. Display the menu.
3. Ask the user to choose Encrypt, Decrypt, or Exit.
4. If Encrypt: ask for file path and password; encrypt and save output.
5. If Decrypt: ask for encrypted file path and password; decrypt and save output.
6. If Exit: stop the program.
7. Otherwise display an invalid-choice message.
8. Repeat the menu until Exit is selected.

## 8. Conclusion
SecureVault Lite demonstrates file handling, functions, loops, conditions, exception handling, and the use of a cryptography library in a simple practical application.
