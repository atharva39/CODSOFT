import sqlite3
import streamlit as st

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
def add_task(task):
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (task,))
    conn.commit()
    st.success("Task added successfully!")

# Function to mark a task as completed
def complete_task(task_id):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    st.success("Task marked as completed!")

# Function to mark a task as incomplete
def incomplete_task(task_id):
    cursor.execute("UPDATE tasks SET completed = 0 WHERE id = ?", (task_id,))
    conn.commit()
    st.success("Task marked as incomplete!")

# Function to delete a task
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

    # Update the IDs in the database to ensure sequential numbering
    cursor.execute("SELECT id FROM tasks ORDER BY id")
    current_ids = [row[0] for row in cursor.fetchall()]

    for i, current_id in enumerate(current_ids, start=1):
        cursor.execute("UPDATE tasks SET id = ? WHERE id = ?", (i, current_id))
    conn.commit()

    st.success("Task deleted successfully!")

# Function to update a task
def update_task(task_id, new_description):
    cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_description, task_id))
    conn.commit()
    st.success("Task updated successfully!")

# Function to display tasks
def display_tasks():
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()

    if tasks:
        st.write("Tasks:")
        for task in tasks:
            status = "Completed" if task[2] else "Incomplete"
            st.write(f"{task[0]}. {task[1]} - {status}")

        st.write("\n\n")
        st.write("---")
        st.write("\n\n")
        st.write("Actions:")
        task_id = st.number_input("Enter the task ID:", min_value=1)
        if st.button("Complete"):
            complete_task(task_id)
        if st.button("Incomplete"):
            incomplete_task(task_id)
        if st.button("Delete"):
            delete_task(task_id)
        st.write("\n\n")
        st.write("---")
        st.write("\n\n")
        st.write("Update Task:")
        new_description = st.text_input("Enter the updated task description:")
        if st.button("Update"):
            if new_description:
                update_task(task_id, new_description)
    else:
        st.warning("No tasks found!")

# Main function to run the Streamlit app
def main():
    st.title("To-Do List Application")

    menu = ["Add Task", "Display Tasks"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Task":
        task = st.text_input("Enter the task:")
        if st.button("Add"):
            add_task(task)
    elif choice == "Display Tasks":
        display_tasks()

if __name__ == "__main__":
    main()
