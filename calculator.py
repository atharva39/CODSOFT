# Written by Atharva Patil on 21th April 2024
# Task 2: Calculator given by CodSoft
import tkinter as tk

# Function to update the input field when buttons are clicked
def button_click(number):
    current = entry_display.get()
    if current == "Error":
        entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, number)

# Function to perform calculation when "=" button is clicked
def button_equal():
    try:
        result = eval(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, "Error")

# Function to clear the input field when "C" button is clicked
def button_clear():
    entry_display.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create entry widget to display input and results with larger font size
entry_display = tk.Entry(root, width=35, borderwidth=5, font=("Arial", 20))  # Increased font size
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
button_labels = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create buttons and arrange them in a grid layout
for label, row, column in button_labels:
    if label == "C":
        button = tk.Button(root, text=label, padx=20, pady=15, font=("Arial", 12), command=button_clear)
    else:
        button = tk.Button(root, text=label, padx=20, pady=15, font=("Arial", 12),
                        command=lambda label=label: button_click(label) if label != "=" else button_equal())
    button.grid(row=row, column=column, padx=5, pady=5)

# Run the main event loop
root.mainloop()
