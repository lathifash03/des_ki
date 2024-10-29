# des_keygen.py

# Permutasi Pilihan 1 (PC-1)
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

# Permutasi Pilihan 2 (PC-2)
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

# Shift untuk setiap round
SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def permute(key, table):
    return ''.join([key[i - 1] for i in table])

def shift_left(key, num_shifts):
    return key[num_shifts:] + key[:num_shifts] #modifikasi kunci pada setiap round. 

def generate_keys(initial_key):
    keys = []
    permuted_key = permute(initial_key, PC1)
    
    C, D = permuted_key[:28], permuted_key[28:]
    
    for shift in SHIFTS:
        C = shift_left(C, shift)
        D = shift_left(D, shift)
        combined_key = C + D
        round_key = permute(combined_key, PC2)
        keys.append(round_key)
    
    return keys
