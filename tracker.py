from datetime import datetime

import json

tasks = []

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return[]

def save_tasks(tasks_list):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks_list, file, ensure_ascii=False, indent=4)

def show_tasks():
        print("Ваши задачи: ")
        if not tasks:
            print("Список пуст!")
        else:
            for i, task in enumerate(tasks, 1):
                status_mark = "[x]" if task.get("status") == "done" else "[]"
                print(f"{i}. {status_mark} {task['title']} (Добавлено: {task['date']})")
def add_tasks():
        new_task = input("Что добавить? ")
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        task_dict = {"title": new_task, "date": now, "status": "active"}
        tasks.append(task_dict)
        save_tasks(tasks)
        print("Задача добавлена!")

def delete_tasks():
        print("Ваши задачи: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} (добавлено: {task['date']})")
        choice = input("Какую задачу удаляем? (введите номер): ")
        if not choice.isdigit():
            print("Ошибка! Нужно ввести число! ")
        else:
            choice_num = int(choice)
            if 1 <= choice_num <= len (tasks):
                deleted_task = tasks.pop(choice_num - 1)
                save_tasks(tasks)
                print(f"Задача '{deleted_task['title']}' успешно удалена! ")
            else:
                print("Задачи с таким порядковым номером не существует! ")

def clear_tasks():
        confirm = input("Вы уверены? (д/н): ")
        if confirm.lower() == "д":
            tasks.clear()
            save_tasks(tasks)
            print("Все задачи удалены! ")
        else:
            print("Действие отменено. ")

def edit_tasks():
    if not tasks:
        print("Список пуст!")
        return
    print("Ваши задачи:")
    for i, task in enumerate(tasks, 1):
        status_mark = "[x]" if task.get("status") == "done" else "[ ]"
        print(f"{i}. {status_mark} {task['title']}")
    choice = int(input("Какую задачу отменить?"))
    if not choice.isdigit:
        print("Ошибка! Введите число!")
    else:
        if 1 <= choice <= len(tasks):
            if tasks[choice - 1].get("status") == "done":
                tasks[choice - 1]["status"] = "active"
                print("Задача снова активна!")
            else:
                tasks[choice - 1]["status"] = "done"
                print("Задача выполнена!")
            save_tasks(tasks)
        else:
            print("Задачи с таким номером не существует! ")

def toggle_status():
    if not tasks:
        print("Список пуст!")
        return
    print("Ваши задачи: ")
    for i, task in enumerate(tasks, 1):
                status_mark = "[x]" if task.get("status") == "done" else "[]"
                print(f"{i}. {status_mark} {task['title']} (Добавлено: {task['date']})")
    choice = input("Какую задачу отменить? (введите число):")
    if not choice.isdigit():
        print("Ошибка! Введите число!")
    else:
        choice_num = int(choice)
        if 1 <= choice_num <= len(tasks):
            if tasks[choice_num - 1].get("status") == "done":
                tasks[choice_num - 1]["status"] = "active"
                print("Задача снова активна!")
            else:
                tasks[choice_num - 1]["status"] = "done"
                print("Задача выполнена!")
            save_tasks(tasks)
        else:
            print("Задачи с таким номером не существует!")

def search_task():
    zapr = input("Введите слово для поиска: ").lower()
    found = False

    print("\nРезультаты поиска:")
    for i, task in enumerate(tasks, 1):
        if zapr in task['title'].lower():
            status_mark = "[x]" if task.get("status") == "done" else "[ ]"
            print(f"{i}. {status_mark} {task['title']} (Добавлено: {task['date']})")
            found = True
    if not found:
        print("Ничего не найдено.")

tasks = load_tasks()

while True:
    print("1. Показать задачи\n2. Добавить задачу\n3. Удалить задачу\n4. Редактировать задачу\n5. Найти задачу\n6. Отметить выполненной\n7. Очистить всё\n8. Выход")
    
    zad = input("Выберите число (1-8): ")
    
    if zad == "8":
        print("Всего доброго!")
        break
    elif zad == "1":
        show_tasks()
    elif zad == "2":
        add_tasks()
    elif zad == "3":
        delete_tasks()
    elif zad == "4":
        edit_tasks()
    elif zad == "6":
        toggle_status()
    elif zad == "5":
        search_task()
    elif zad == "7":
        clear_tasks()
    else:
        print("Такого пункта нет. введи 1-8.")