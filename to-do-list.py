# Written by Atharva Vivek Patil on 15th April 2024
# Task 1 : To-Do List given by CodSoftt
import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Create the tasks table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        description TEXT,
        completed INTEGER DEFAULT 0
    )
""")
conn.commit()

# Function to add a task
def add_task():
    task = entry_task.get()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (task,))
    conn.commit()
    display_tasks()
    entry_task.delete(0, tk.END)

# Function to delete a task
def delete_task():
    task_id = selected_task.get()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    display_tasks()

# Function to toggle task completion status
def toggle_completion():
    task_id = selected_task.get()
    cursor.execute("SELECT completed FROM tasks WHERE id = ?", (task_id,))
    completion_status = cursor.fetchone()[0]
    new_status = 0 if completion_status else 1
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    display_tasks()

    # Change button text based on new completion status
    if new_status == 1:
        button_toggle.config(text="Mark as Incomplete")
    else:
        button_toggle.config(text="Mark as Completed")

# Function to export tasks to a .txt file
def export_tasks():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            cursor.execute("SELECT description, completed FROM tasks")
            tasks = cursor.fetchall()
            for task in tasks:
                status = "Completed" if task[1] else "Incomplete"
                file.write(f"{task[0]} - {status}\n")
        messagebox.showinfo("Export Successful", "Tasks exported to .txt file successfully!")

# Function to display tasks
def display_tasks():
    task_list.delete(0, tk.END)
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        status = "Completed" if task[2] else "Incomplete"
        task_list.insert(tk.END, f"{task[0]}. {task[1]} - {status}")

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("To-Do List")

# Configure aesthetic colors
bg_color = "#ADD8E6"  # Soft blue
button_color = "#D8BFD8"  # Dusty rose

# Set aesthetic background color
root.configure(bg=bg_color)

# Entry for adding tasks
entry_task = tk.Entry(root, width=50, font=("Arial", 12))
entry_task.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Button to add task
button_add = tk.Button(root, text="Add Task", command=add_task, bg=button_color, fg="black", font=("Arial", 12))
button_add.grid(row=0, column=2, padx=5, pady=10)

# Listbox to display tasks
task_list = tk.Listbox(root, width=80, font=("Arial", 12))
task_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Button to delete task
button_delete = tk.Button(root, text="Delete Task", command=delete_task, bg=button_color, fg="black", font=("Arial", 12))
button_delete.grid(row=2, column=0, padx=5, pady=10, sticky="w")

# Button to export tasks to a .txt file
button_export = tk.Button(root, text="Export to .txt", command=export_tasks, bg=button_color, fg="black", font=("Arial", 12))
button_export.grid(row=2, column=1, padx=5, pady=10)

# Button to toggle task completion status
button_toggle = tk.Button(root, text="Toggle Completion", command=toggle_completion, bg=button_color, fg="black", font=("Arial", 12))
button_toggle.grid(row=2, column=2, padx=5, pady=10, sticky="e")

# Selected task variable
selected_task = tk.StringVar()

# Set up selection event for the listbox
def on_select(event):
    try:
        index = task_list.curselection()[0]
        selected_task.set(task_list.get(index).split(".")[0])
        task_id = selected_task.get()
        cursor.execute("SELECT completed FROM tasks WHERE id = ?", (task_id,))
        completion_status = cursor.fetchone()[0]
        button_toggle.config(text="Mark as Incomplete" if completion_status else "Mark as Completed")
    except IndexError:
        pass

task_list.bind("<<ListboxSelect>>", on_select)

# Display tasks initially
display_tasks()

# Run the Tkinter event loop
root.mainloop()
