from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Apply the encryption operation (adding the key to each pixel)
    encrypted_array = (image_array + key) % 256  # Ensure the values stay within the valid range
    
    # Convert the numpy array back to an image
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    
    # Save the encrypted image
    encrypted_image.save(output_image_path)
    print(f"Encrypted image saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Apply the decryption operation (subtracting the key from each pixel)
    decrypted_array = (image_array - key) % 256  # Ensure the values stay within the valid range
    
    # Convert the numpy array back to an image
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    
    # Save the decrypted image
    decrypted_image.save(output_image_path)
    print(f"Decrypted image saved to {output_image_path}")

def get_valid_output_path(prompt):
    import os
    while True:
        path = input(prompt)
        if os.path.splitext(path)[1] in ['.png', '.jpg', '.jpeg', '.bmp']:
            return path
        else:
            print("Please enter a valid output file path with an image extension (e.g., .png, .jpg).")

if __name__ == "__main__":
    choice = int(input("Enter 1 to encrypt and 2 to decrypt: "))
    input_image_path = input("Enter the path to the input image: ")
    output_image_path = get_valid_output_path("Enter the path to save the output image (with extension .png or .jpg): ")
    key = int(input("Enter an encryption key (0-255): "))

    if choice == 1:
        encrypt_image(input_image_path, output_image_path, key)
    elif choice == 2:
        decrypt_image(input_image_path, output_image_path, key)
    else:
        print("Invalid choice")
