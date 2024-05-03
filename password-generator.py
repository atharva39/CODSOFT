# Written by Atharva Vivek Patil on 4th May 2024
# Task 3 : Password Generator given by CodSoft
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length, include_special_chars=True):
    """
    Generates a random password of specified length.
    
    Parameters:
    - length: int, length of the password
    - include_special_chars: bool, whether to include special characters
    
    Returns:
    - str, generated password
    """
    # Define character set
    chars = string.ascii_letters + string.digits
    if include_special_chars:
        chars += string.punctuation
    
    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password

def generate_button_click():
    # Callback function for generate button click
    
    # Get password length from entry widget
    length_str = length_entry.get()
    
    # Validate password length input
    try:
        length = int(length_str)
        if length < 8:
            messagebox.showinfo("Info", "Default password length is 8. You cannot select a length below this.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the password length.")
        return
    
    # Get special characters checkbox value
    include_special_chars = special_chars_var.get()
    
    # Generate password
    password = generate_password(length, include_special_chars)
    
    # Update label with generated password
    password_label.config(text="Generated Password: " + password)
    
    # Enable the copy to clipboard button
    copy_button.config(state="normal")

def copy_to_clipboard():
    # Callback function for copy to clipboard button click
    
    password = password_label.cget("text")[18:]  # Get the generated password from the label text
    pyperclip.copy(password)  # Copy the password to the clipboard
    messagebox.showinfo("Info", "Password copied to clipboard.")  # Show a message to confirm

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Password length label and entry widget
length_label = tk.Label(root, text="Enter the desired length of the password (default is 8):")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Special characters checkbox
special_chars_var = tk.BooleanVar(value=True)
special_chars_check = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var)
special_chars_check.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_button_click)
generate_button.pack()

# Label to display generated password
password_label = tk.Label(root, text="")
password_label.pack()

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.pack()

# Run the main event loop
root.mainloop()
