import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Lista de Tareas")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        
        self.create_widgets()
        self.setup_layout()
        self.configure_responsive_grid()
        self.setup_styles()
        
        self.init_instructions()

    def create_widgets(self):
        self.entry_task = ttk.Entry(self.root, width=40, font=('Arial', 12))
        self.button_add = ttk.Button(self.root, text="Agregar Tarea", command=self.add_task, style='C.TButton')
        self.listbox_tasks = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=40, height=10, font=('Arial', 12))
        self.button_complete = ttk.Button(self.root, text="Marcar como Completada", command=self.complete_task, style='C.TButton')
        self.button_delete = ttk.Button(self.root, text="Eliminar Completadas", command=self.delete_task, style='C.TButton')

    def setup_layout(self):
        self.entry_task.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.button_add.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.button_complete.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.button_delete.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    def configure_responsive_grid(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)

    def setup_styles(self):
        self.root.tk_setPalette(background='#f0f0f0', foreground='black',
                                activeBackground='#4CAF50', activeForeground='white')

        style = ttk.Style()
        style.configure('C.TButton', font=('Arial', 12), background='#2196F3', foreground='black', padding=10)

    def init_instructions(self):
        messagebox.showinfo("Bienvenido", "¡Bienvenido a la Aplicación de Lista de Tareas!\n\nPara comenzar, escribe una tarea en el campo de entrada y haz clic en 'Agregar Tarea'.")

    def add_task(self):
        task = self.entry_task.get()
        if task.strip() != "":
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía")

    def complete_task(self):
        selected_tasks = self.listbox_tasks.curselection()
        for i in selected_tasks[::-1]:
            task = self.listbox_tasks.get(i)
            self.listbox_tasks.delete(i)
            self.listbox_tasks.insert(tk.END, f"{task} - Completada")

    def delete_task(self):
        selected_tasks = self.listbox_tasks.curselection()
        for i in selected_tasks[::-1]:
            task = self.listbox_tasks.get(i)
            if " - Completada" in task:
                self.listbox_tasks.delete(i)
            else:
                messagebox.showwarning("Advertencia", "Selecciona solo tareas completadas para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
