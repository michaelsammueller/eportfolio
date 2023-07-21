"""
    Contains the UI and Affine Cipher classes
"""
# Imports
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Affine TXT Encryption")

        # Create an instance of the Affine class
        self.affine = Affine()

        # Set application windwow size
        self.root.geometry("400x200")

        # Create UI elements
        self.label = tk.Label(root, text="File to encrypt:")
        self.label.place(x=20, y=20)

        # Browse and filepath logic
        self.filepath = tk.StringVar()
        self.filepath_entry = tk.Entry(root, textvariable=self.filepath, width=40)
        self.filepath_entry.place(x=20, y=50)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse)
        self.browse_button.place(x=280, y=50)

        # Encrypt button
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.place(x=160, y=100)

    # 'browse' method
    def browse(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.filepath.set(filepath)
    
    # 'encrypt' method    
    def encrypt(self):
        filepath = self.filepath.get()
        if not filepath:
            messagebox.showwarning("Warning", "Please select a file to encrypt!")
            return
        try:
            with open(filepath, "r") as file:
                text = file.read()
                encrypted_text = self.affine.encrypt(text)
                
            # Store encrypted content in new .txt file
            directory = os.path.dirname(filepath)
            new_path = os.path.join(directory, "encrypted.txt")
            with open(new_path, "w") as file:
                file.write(encrypted_text)
                
            messagebox.showinfo("Success", f"File encrypted successfully at {new_path}")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occured: {e}")

class Affine(object):
    DIE = 128
    KEY = (7, 3, 55)

    def encryptChar(self, char):
        K1, K2, kI = self.KEY
        return chr((K1 * ord(char) + K2) % self.DIE)
    
    def encrypt(self, string):
        return "".join(map(self.encryptChar, string))
    
    def decryptChar(self, char):
        K1, K2, KI = self.KEY
        return chr(KI * (ord(char) - K2) % self.DIE)
    
    def decrypt(self, string):
        return "".join(map(self.decryptChar, string))


root = tk.Tk()
app = UI(root)
root.mainloop()