import tkinter as tk
from tkinter import messagebox

# Initialize the to-do list
todo_list = []

def add_task():
    """Add a task to the to-do list."""
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Input Error", "Task cannot be empty!")
        return
    todo_list.append({'task': task, 'completed': False})
    task_entry.delete(0, tk.END)
    update_task_list()

def update_task_list():
    """Update the listbox with tasks."""
    tasks_listbox.delete(0, tk.END)
    for i, task in enumerate(todo_list):
        status = "✓" if task['completed'] else "✗"
        tasks_listbox.insert(tk.END, f"{i + 1}. {task['task']} [{status}]")

def mark_task_completed():
    """Mark a selected task as completed."""
    try:
        selected_index = tasks_listbox.curselection()[0]
        todo_list[selected_index]['completed'] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def exit_app():
    """Exit the application."""
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task entry and add button
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

# Buttons to mark tasks completed and exit
mark_completed_button = tk.Button(root, text="Mark as Completed", command=mark_task_completed)
mark_completed_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

# Run the application
root.mainloop()
