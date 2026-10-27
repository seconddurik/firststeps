import tkinter as tk
import json
from datetime import datetime

try:
    with open("tasks.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)
except:
    tasks = []

def add_task():
    text = task_entry.get()
    if not text.strip():
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_task = {"title": text, "date": now, "status": "active"}
    tasks.append(new_task)

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
    task_entry.delete(0, tk.END)
    update_listbox()

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "[x]" if task.get("status") == "done" else "[ ]"
        task_listbox.insert(tk.END, f"{status} {task['title']} ({task['date']})")

def delete_task():
    selected = task_listbox.curselection()
    
    if not selected:
        return
    
    index = selected[0]
    tasks.pop(index)
    
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
    
    update_listbox()

def toggle_status():
    selected = task_listbox.curselection()
    
    if not selected:
        return
    
    index = selected[0]
    task = tasks[index]
    
    if task.get("status") == "done":
        task["status"] = "active"
    else:
        task["status"] = "done"
    
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
    
    update_listbox()

root = tk.Tk()
root.title("Трекер задач")
root.geometry("400x500")

#поле ввода
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

#кнопка добавить
add_button = tk.Button(root, text="Добавить задачу", width=20, command=add_task)
add_button.pack(pady=5)

#список
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

#кнопки действия; frame, чтобы кнопки стояли в ряд
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

#кнопки внутри рамки
done_button = tk.Button(button_frame, text="Выполнено", width=12, command=toggle_status)
done_button.pack(side=tk.LEFT, padx=5)
delete_button = tk.Button(button_frame, text="Удалить", width=12, command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

update_listbox()
root.mainloop()