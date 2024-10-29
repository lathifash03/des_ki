# main.py

from des import des_encrypt, des_decrypt

# Fungsi Konversi Teks ke Biner dan Sebaliknya
def text_to_binary(text):
    binary_text = ''.join(format(ord(c), '08b') for c in text)
    return binary_text

def binary_to_text(binary):
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text
# Fungsi Padding
def pad_binary(binary_text, block_size=64):
    padding_length = block_size - (len(binary_text) % block_size)
    padding = '0' * padding_length
    return binary_text + padding

def remove_padding(binary_text):
    return binary_text.rstrip('0')

# Fungsi Input Binary 64-bit
def binary_input(prompt):
    while True:
        inp = input(prompt)
        if len(inp) == 64 and all(c in '01' for c in inp):
            return inp
        else:
            print("Input harus berupa 64-bit binary string.")

def main():
    mode = input("Pilih mode (encrypt/decrypt): ").strip().lower()
    key = binary_input("Masukkan kunci (64-bit binary): ")
    
    if mode == "encrypt":
        input_mode = input("Ingin mengenkripsi teks atau biner? (text/binary): ").strip().lower()
        
        if input_mode == "text":
            plaintext = input("Masukkan plaintext (teks): ").strip()
            
            # Konversi teks ke biner
            binary_plaintext = text_to_binary(plaintext)
            
            # Tambahkan padding jika diperlukan
            padded_binary = pad_binary(binary_plaintext)
            
            # Lakukan enkripsi dengan DES
            ciphertext = des_encrypt(padded_binary, key)
            print(f"Hasil ciphertext (biner): {ciphertext}")
            ciphertext_hex = hex(int(ciphertext, 2))[2:]
            print(f"Hasil ciphertext (hex): {ciphertext_hex}")
        
        elif input_mode == "binary":
            plaintext = binary_input("Masukkan plaintext (64-bit binary): ")
            ciphertext = des_encrypt(plaintext, key)
            print(f"Hasil ciphertext: {ciphertext}")
        
        else:
            print("Mode input tidak valid. Pilih antara 'text' atau 'binary'.")

    elif mode == "decrypt":
        input_mode = input("Ingin mendekripsi teks atau biner? (text/binary): ").strip().lower()
        
        if input_mode == "text":
            ciphertext_hex = input("Masukkan ciphertext (hex): ").strip()
            
            # Konversi hex ke biner
            ciphertext_binary = bin(int(ciphertext_hex, 16))[2:].zfill(64)
            
            # Lakukan dekripsi
            decrypted_binary = des_decrypt(ciphertext_binary, key)
            
            # Hapus padding dan konversi kembali ke teks
            unpadded_binary = remove_padding(decrypted_binary)
            decrypted_text = binary_to_text(unpadded_binary)
            print(f"Hasil dekripsi (teks): {decrypted_text}")
        
        elif input_mode == "binary":
            ciphertext = binary_input("Masukkan ciphertext (64-bit binary): ")
            plaintext = des_decrypt(ciphertext, key)
            print(f"Hasil plaintext: {plaintext}")
        
        else:
            print("Mode input tidak valid. Pilih antara 'text' atau 'binary'.")

    else:
        print("Mode tidak valid. Pilih antara encrypt atau decrypt.")

if __name__ == "__main__":
    main()
