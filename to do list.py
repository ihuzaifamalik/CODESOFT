import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        # Delete Task Button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Clear the entry field
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete the task: {selected_task}?")
            if confirm:
                self.task_listbox.delete(selected_index)
                self.tasks.remove(selected_task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
