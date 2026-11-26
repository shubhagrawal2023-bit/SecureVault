# SecureVault Lite — Beginner Python Project

A simple menu-driven file encryption and decryption program suitable for a first-year Python project.

## Features
- Menu with Encrypt, Decrypt, and Exit
- Password-based encryption
- Works with common files (text, PDF, images, CSV, etc.)
- Wrong password or damaged file is detected
- Original file is preserved

## Requirements
- Python installed on Windows
- `cryptography` package

## Install
Open the VS Code terminal in this folder and run:

```powershell
py -m pip install cryptography
```

## Run

```powershell
py main.py
```

## How to demonstrate
1. Create a text file called `sample.txt`.
2. Run the program and choose option 1.
3. Enter `sample.txt` and a password.
4. The program creates `sample.txt.enc`.
5. Choose option 2 and enter the encrypted file path and same password.
6. The restored file is created with a `restored_` prefix.
7. Try a wrong password to demonstrate error handling.

## Concepts used
- Functions
- `while` loop and `if/elif`
- User input and output
- File paths using `pathlib`
- Reading and writing bytes
- Password-based key derivation
- Exception handling
- A third-party encryption library

## Security note
This is a learning project, not a professionally audited product. Use test files and never test with real wallet/private-key files. Forgotten passwords cannot be recovered.
