# main.py
from des import des_encrypt, des_decrypt

def binary_input(prompt):
    # Fungsi sederhana untuk mendapatkan input dalam bentuk biner 64-bit
    while True:
        value = input(prompt)
        if len(value) == 64 and set(value).issubset({'0', '1'}):
            return value
        else:
            print("Input harus dalam format biner 64-bit.")

if __name__ == "__main__":
    key = binary_input("Masukkan kunci (64-bit biner): ")
    plaintext = binary_input("Masukkan plaintext (64-bit biner): ")

    # Enkripsi
    ciphertext = des_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    # Dekripsi
    decrypted_text = des_decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
