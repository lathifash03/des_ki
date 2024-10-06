# DES Encryption Implementation

This project provides a Python implementation of the Data Encryption Standard (DES) algorithm. DES is a symmetric-key block cipher that encrypts data in 64-bit blocks using a 56-bit key.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Features

- Encryption and decryption of 64-bit data blocks
- Key generation for the encryption process
- Implementation of the Feistel network structure
- Support for initial and final permutations, as well as S-box substitution

## Installation

To run this project, ensure you have Python installed on your system. You can clone this repository and install the required dependencies using pip.

```bash
git clone <repository_url>
cd <repository_directory>
pip install -r requirements.txt
from des import des_encrypt, des_decrypt

key = "your_key_here"  # 64-bit key (8 bytes)
plaintext = "your_plaintext_here"  # 64-bit plaintext (8 bytes)

# Encrypting the plaintext
ciphertext = des_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

# Decrypting the ciphertext
decrypted_text = des_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")

```
.
├── des.py                # Main implementation of DES algorithm
├── des_keygen.py         # Key generation module
├── utils.py              # Utility functions for permutations, expansions, etc.
├── requirements.txt      # Dependencies for the project
└── README.md             # Project documentation
Functionality

Key Functions
des_encrypt(plaintext, key): Encrypts the provided plaintext using the specified key.
des_decrypt(ciphertext, key): Decrypts the provided ciphertext using the specified key.
generate_keys(key): Generates subkeys from the main key for each round of encryption.
feistel_function(R, key): Implements the Feistel function, which includes expansion, XOR, substitution using S-boxes, and permutation.
S-Boxes
The S-boxes used in the DES implementation are defined in the S_BOX variable and consist of 8 substitution boxes. Each box takes a 6-bit input and produces a 4-bit output.
