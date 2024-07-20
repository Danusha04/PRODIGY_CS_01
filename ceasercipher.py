def encrypt(text, shift):
    """
    Encrypts the text using Caesar Cipher with the given shift.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """
    Decrypts the text using Caesar Cipher with the given shift.
    """
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        result = encrypt(text, shift)
        print(f"Encrypted message: {result}")
    elif choice == 'd':
        result = decrypt(text, shift)
        print(f"Decrypted message: {result}")
    else:
        print("Invalid choice! Please choose 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
