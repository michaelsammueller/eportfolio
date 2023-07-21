
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from cryptography.fernet import Fernet

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("AES TXT Encryption")
        self.aes = AES()

        self.root.geometry("400x200")

        self.label = tk.Label(root, text="File to encrypt:")
        self.label.place(x=20, y=20)

        self.filepath = tk.StringVar()
        self.filepath_entry = tk.Entry(root, textvariable=self.filepath, width=40)
        self.filepath_entry.place(x=20, y=50)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse)
        self.browse_button.place(x=280, y=50)

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.place(x=160, y=100)

    def browse(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.filepath.set(filepath)
    
    def encrypt(self):
        filepath = self.filepath.get()
        if not filepath:
            messagebox.showwarning("Warning", "Please select a file to encrypt!")
            return
        try:
            with open(filepath, "r") as file:
                text = file.read()
                encrypted_text = self.aes.encrypt(text)
                
            directory = os.path.dirname(filepath)
            new_path = os.path.join(directory, "encrypted.txt")
            with open(new_path, "wb") as file:
                file.write(encrypted_text)
                
            messagebox.showinfo("Success", f"File encrypted successfully at {new_path}")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occured: {e}")

class AES:
    def __init__(self):
        # Generate a key for Fernet encryption
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
    
    def encrypt(self, text):
        encoded_text = text.encode()
        encrypted_text = self.cipher.encrypt(encoded_text)
        return encrypted_text

    # This method is for future use if you decide to implement decryption
    def decrypt(self, encrypted_text):
        decrypted_text = self.cipher.decrypt(encrypted_text)
        return decrypted_text.decode()

root = tk.Tk()
app = UI(root)
root.mainloop()
