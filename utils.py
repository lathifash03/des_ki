# utils.py

# Tabel permutasi awal
INITIAL_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Tabel permutasi akhir
FINAL_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Tabel permutasi P
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# Tabel ekspansi (Expansion/Permutation Table)
EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# Fungsi untuk permutasi
def permute(block, table):
    return ''.join([block[i - 1] for i in table])

# Fungsi untuk memperluas blok dari 32-bit menjadi 48-bit
def expand(R):
    return permute(R, EXPANSION_TABLE)

# Fungsi untuk melakukan XOR antara dua bit
def xor_bits(bits1, bits2):
    return ''.join(['1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2)])

# Fungsi substitusi menggunakan S-Box
def substitute(xor_output):
    result = ''
    for i in range(0, 48, 6):
        block = xor_output[i:i + 6]
        row = int(block[0] + block[5], 2)  # Mengambil bit paling kiri dan paling kanan untuk menentukan baris
        col = int(block[1:5], 2)          # Mengambil 4 bit tengah untuk menentukan kolom
        s_box_value = S_BOX[i // 6][row][col]  # Mengambil nilai dari S-Box
        result += format(s_box_value, '04b')    # Mengonversi ke biner 4 bit
    return result


def permute(block, table):
    return ''.join([block[i - 1] for i in table])

# Fungsi permutasi (IP, FP)
def initial_permutation(block):
    return permute(block, INITIAL_PERMUTATION)

def final_permutation(block):
    return permute(block, FINAL_PERMUTATION)
