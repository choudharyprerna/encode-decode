import tkinter as tk

# Function to encrypt the message
def encrypt_message(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_message += char
    return encrypted_message

# Function to decrypt the message
def decrypt_message(encrypted_message, key):
    return encrypt_message(encrypted_message, 26 - key) # Decrypting is just encrypting with the inverse key

# Function to handle encryption button click
def encrypt_button_clicked():
    message = entry_message.get()
    key = int(entry_key.get())
    encrypted = encrypt_message(message, key)
    entry_output.delete(0, tk.END)
    entry_output.insert(tk.END, encrypted)

# Function to handle decryption button click
def decrypt_button_clicked():
    encrypted_message = entry_message.get()
    key = int(entry_key.get())
    decrypted = decrypt_message(encrypted_message, key)
    entry_output.delete(0, tk.END)
    entry_output.insert(tk.END, decrypted)

# Create the main window
root = tk.Tk()
root.title("Message Encoder/Decoder")

# Create GUI elements
label_message = tk.Label(root, text="Enter Message:")
entry_message = tk.Entry(root)

label_key = tk.Label(root, text="Enter Key (0-25):")
entry_key = tk.Entry(root)

btn_encrypt = tk.Button(root, text="Encrypt", command=encrypt_button_clicked)
btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt_button_clicked)

label_output = tk.Label(root, text="Result:")
entry_output = tk.Entry(root)

# Place GUI elements in the window
label_message.pack()
entry_message.pack()

label_key.pack()
entry_key.pack()

btn_encrypt.pack()
btn_decrypt.pack()

label_output.pack()
entry_output.pack()

# Start the main loop
root.mainloop()