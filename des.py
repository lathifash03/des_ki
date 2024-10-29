# des.py

from des_keygen import generate_keys
from utils import initial_permutation, final_permutation, expand, xor_bits, feistel_function

def des_encrypt(plaintext, key):
    # Initial Permutation
    plaintext = initial_permutation(plaintext)
    
    # Split ke L dan R
    L, R = plaintext[:32], plaintext[32:]
    
    # Generate subkeys
    subkeys = generate_keys(key)
    
    # 16 Rounds Feistel Network
    for i in range(16):
        L_next = R
        R_next = xor_bits(L, feistel_function(R, subkeys[i]))
        L, R = L_next, R_next
    
    # Swap terakhir dan gabungkan L dan R
    combined = R + L
    ciphertext = final_permutation(combined)
    
    return ciphertext

def des_decrypt(ciphertext, key):
    # Initial Permutation
    ciphertext = initial_permutation(ciphertext)
    
    # Split ke L dan R
    L, R = ciphertext[:32], ciphertext[32:]
    
    # Generate subkeys
    subkeys = generate_keys(key)
    
    # 16 Rounds Feistel Network (dengan urutan subkey terbalik)
    for i in range(16):
        L_next = R
        R_next = xor_bits(L, feistel_function(R, subkeys[15 - i]))
        L, R = L_next, R_next
    
    # Swap terakhir dan gabungkan L dan R
    combined = R + L
    plaintext = final_permutation(combined)
    
    return plaintext
