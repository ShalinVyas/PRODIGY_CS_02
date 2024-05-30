import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Function to simulate encryption (for demonstration purposes)
def encrypt_image(input_path, output_path):
    # Simulate encryption by renaming the file
    os.rename(input_path, output_path)

# Function to simulate decryption (for demonstration purposes)
def decrypt_image(input_path, output_path):
    # Simulate decryption by renaming the file
    os.rename(input_path, output_path)

# Function to handle the encrypt button click
def handle_encrypt():
    input_path = filedialog.askopenfilename(title="Select an image to encrypt")
    if input_path:
        output_path = filedialog.asksaveasfilename(title="Select where to save the encrypted image")
        if output_path:
            try:
                encrypt_image(input_path, output_path)
                messagebox.showinfo("Success", "Image encrypted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to encrypt image: {e}")

# Function to handle the decrypt button click
def handle_decrypt():
    input_path = filedialog.askopenfilename(title="Select an image to decrypt")
    if input_path:
        output_path = filedialog.asksaveasfilename(title="Select where to save the decrypted image")
        if output_path:
            try:
                decrypt_image(input_path, output_path)
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
