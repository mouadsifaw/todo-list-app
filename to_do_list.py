import tkinter as tk
from tkinter import messagebox
import json

# Global todo list variable
todo_list = []

# Load tasks from a JSON file (if exists)
def load_tasks():
    global todo_list
    try:
        with open("tasks.json", "r") as file:
            todo_list = json.load(file)
    except FileNotFoundError:
        todo_list = []
    view_tasks()

# Save tasks to a JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(todo_list, file)
    print("Tasks saved successfully.")

# Add a new task to the list
def add_task():
    task = task_entry.get()
    if task:
        todo_list.append({'task': task, 'completed': False, 'priority': priority_var.get()})
        save_tasks()
        task_entry.delete(0, tk.END)
        view_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Mark a task as completed
def mark_task_completed():
    task_number = int(task_number_entry.get())
    if 0 < task_number <= len(todo_list):
        todo_list[task_number - 1]['completed'] = True
        save_tasks()
        view_tasks()
    else:
        messagebox.showerror("Error", "Invalid task number.")

# Delete a task
def delete_task():
    task_number = int(task_number_entry.get())
    if 0 < task_number <= len(todo_list):
        del todo_list[task_number - 1]
        save_tasks()
        view_tasks()
    else:
        messagebox.showerror("Error", "Invalid task number.")

# Edit a task
def edit_task():
    task_number = int(task_number_entry.get())
    new_task = task_entry.get()
    if 0 < task_number <= len(todo_list) and new_task:
        todo_list[task_number - 1]['task'] = new_task
        save_tasks()
        task_entry.delete(0, tk.END)
        view_tasks()
    else:
        messagebox.showerror("Error", "Invalid task number or empty task.")

# Display tasks with their status
def view_tasks():
    tasks_listbox.delete(0, tk.END)
    for i, task in enumerate(todo_list):
        status = "Completed" if task['completed'] else "Not Completed"
        tasks_listbox.insert(tk.END, f"{i + 1}. {task['task']} - {status} (Priority: {task['priority']})")

# Create main window
root = tk.Tk()
root.title("To-Do List Application")

# UI Elements
task_entry_label = tk.Label(root, text="Task:")
task_entry_label.grid(row=0, column=0, padx=10, pady=5)
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=1, padx=10, pady=5)

priority_var = tk.StringVar(root)
priority_var.set("Medium")  # default value
priority_label = tk.Label(root, text="Priority:")
priority_label.grid(row=1, column=0, padx=10, pady=5)
priority_dropdown = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_dropdown.grid(row=1, column=1, padx=10, pady=5)

task_number_label = tk.Label(root, text="Task Number:")
task_number_label.grid(row=2, column=0, padx=10, pady=5)
task_number_entry = tk.Entry(root, width=5)
task_number_entry.grid(row=2, column=1, padx=10, pady=5)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.grid(row=0, column=2, padx=10, pady=5)

mark_task_completed_button = tk.Button(root, text="Mark as Completed", command=mark_task_completed)
mark_task_completed_button.grid(row=2, column=2, padx=10, pady=5)

edit_task_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_task_button.grid(row=3, column=0, padx=10, pady=5)

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.grid(row=3, column=2, padx=10, pady=5)

tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

# Load tasks on startup
load_tasks()

# Run main loop
root.mainloop()
