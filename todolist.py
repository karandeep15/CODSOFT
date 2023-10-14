#importing the dependencies for our project
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# creating a python class for To-do List App
class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI: To-do List Project")
        self.root.geometry("600x600")
        self.root.configure(bg="Sky blue")

        heading_label = tk.Label(root, text="Task 1", font=("Arial", 12, "bold"))
        heading_label.pack(pady=10)
        
        # Creating a heading for our To-do list python roject
        heading_label = tk.Label(root, text="Python GUI : To-do List Project", font=("Helvetica", 16, "bold"))
        heading_label.pack(pady=20) 

        self.tasks = []

        create_button = tk.Button(root, text="Create Task", command=self.create_task, bg="#4caf50", fg="white", font=("Arial", 12))
        create_button.pack(pady=5)
        heading_label = tk.Label(root, text="Add your tasks in the column below", font=("Helvetica", 10, "bold"))
        heading_label.pack(pady=5) 
        
        self.task_entry = tk.Entry(root, width=20, font=("Arial", 14))
        self.task_entry.pack(pady=30)
        
        update_button = tk.Button(root, text="Update Task", command=self.update_task, bg="orange", fg="white", font=("Arial", 12))
        update_button.pack(pady=5)
        heading_label = tk.Label(root, text="Please select your task from the track list down below to update the task", font=("Helvetica", 10, "bold"))
        heading_label.pack(pady=5)
        
        track_button = tk.Button(root, text="Track Tasks", command=self.track_tasks, bg="#2196f3", fg="white", font=("Arial", 12))
        track_button.pack(pady=5)
        heading_label = tk.Label(root, text="Track List", font=("Helvetica", 14, "bold"))
        heading_label.pack(pady=5)
        
        self.task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
        self.task_listbox.pack(padx=10, pady=10)
        
        heading_label = tk.Label(root, text="Made by Karandeep Singh @ CodSoft", font=("Helvetica", 12, "bold"))
        heading_label.pack(pady=10)

        # Add a simple animation effect to the task list
        self.animate_task_listbox()

    def animate_task_listbox(self):
        for i in range(1, 6):
            self.root.after(i * 100, self.update_task_listbox_animation, i)
    
    def update_task_listbox_animation(self, i):
        self.task_listbox.config(bg="#ffffff" if i % 2 == 0 else "#f0f0f0")
    
    def create_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error!", "Task cannot be left empty!")
    
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index] = updated_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Error!", "Task cannot be left empty!")
        else:
            messagebox.showwarning("Error!", "Please select a task to update!")
    
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def track_tasks(self):
        task_count = len(self.tasks)
        if task_count > 0:
            message = f"You have {task_count} task(s) in your to-do list."
        else:
            message = "You have no tasks in your to-do list, Please add some tasks into the List."
        messagebox.showinfo("Tracking Tasks", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
