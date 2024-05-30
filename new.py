import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image
import numpy as np
import os

# Function to encrypt the image
def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_array = np.array(image)
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    encrypted_image.save(output_image_path)
    print(f"Encrypted image saved to {output_image_path}")

# Function to decrypt the image
def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_array = np.array(image)
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    decrypted_image.save(output_image_path)
    print(f"Decrypted image saved to {output_image_path}")

# Function to handle the encrypt button click
def handle_encrypt():
    input_path = filedialog.askopenfilename(title="Select an image to encrypt")
    if input_path:
        output_path = filedialog.asksaveasfilename(title="Select where to save the encrypted image", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if output_path:
            try:
                key = simpledialog.askinteger("Input", "Enter an encryption key (0-255)", minvalue=0, maxvalue=255)
                if key is not None:
                    encrypt_image(input_path, output_path, key)
                    messagebox.showinfo("Success", "Image encrypted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to encrypt image: {e}")

# Function to handle the decrypt button click
def handle_decrypt():
    input_path = filedialog.askopenfilename(title="Select an image to decrypt")
    if input_path:
        output_path = filedialog.asksaveasfilename(title="Select where to save the decrypted image", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if output_path:
            try:
                key = simpledialog.askinteger("Input", "Enter a decryption key (0-255)", minvalue=0, maxvalue=255)
                if key is not None:
                    decrypt_image(input_path, output_path, key)
                    messagebox.showinfo("Success", "Image decrypted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to decrypt image: {e}")

# Create the main window
root = tk.Tk()
root.title("Encrypt/Decrypt Image")
root.geometry("600x400")

# Create the encrypt button
encrypt_button = tk.Button(root, text="Encrypt", bg="red", fg="white", font=("Arial", 14), command=handle_encrypt)
encrypt_button.pack(pady=20, padx=20, side=tk.LEFT, expand=True)

# Create the decrypt button
decrypt_button = tk.Button(root, text="Decrypt", bg="blue", fg="white", font=("Arial", 14), command=handle_decrypt)
decrypt_button.pack(pady=20, padx=20, side=tk.RIGHT, expand=True)

# Run the application
root.mainloop()
