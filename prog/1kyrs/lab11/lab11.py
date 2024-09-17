import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Пустое поле", "Пожалуйста, введите задачу.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Нет выбранной задачи", "Пожалуйста, выберите задачу для удаления.")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("ToDo")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    font=("Courier New", 12),
    bd=0,
    selectbackground="#a6a6a6"
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(
    root,
    font=("Courier New", 12)
)
entry.pack(pady=10)

add_button = tk.Button(
    root,
    text="Добавить задачу",
    command=add_task
)
add_button.pack(pady=5)

delete_button = tk.Button(
    root,
    text="Удалить задачу",
    command=delete_task
)
delete_button.pack(pady=5)

clear_button = tk.Button(
    root,
    text="Очистить список",
    command=clear_tasks
)
clear_button.pack(pady=5)

root.mainloop()