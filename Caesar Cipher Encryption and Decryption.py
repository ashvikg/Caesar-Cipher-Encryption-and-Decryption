# Caesar Cipher Encryption and Decryption Program
# Author: Your Name
# Topic: Cyber Security - Caesar Cipher

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only encrypt letters
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep spaces and punctuation as is
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result


# Main Program
print("=== Caesar Cipher Encryption & Decryption ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))

encrypted_text = encrypt(message, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("\n--- Results ---")
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_text}")
print(f"Decrypted Message: {decrypted_text}")
