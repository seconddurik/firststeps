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
                print(f"{i}. {task['title']} (Добавлено: {task['date']})")
def add_tasks():
        new_task = input("Что добавить? ")
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        task_dict = {"title": new_task, "date": now}
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
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} (добавлено: {task['date']})")
        choice = input("")
        if not choice.isdigit():
            print("Ошибка!")
        else:
            choice_num = int(choice)
            if 1 <= choice_num <= len(tasks):
                new_title = input("")
                tasks[choice_num - 1]["title"] = new_title
                save_tasks(tasks)
                print("Готово!")
            else:
                print("Нет такого номера!")

tasks = load_tasks()

while True:
    print("1. Показать задачи\n2. Добавить задачу\n3. Выход\n4. Удалить задачу\n5. Редактировать задачу\n6. Очистить всё")
    
    zad = input("Выберите число (1-6): ")
    
    if zad == "3":
        print("Всего доброго!")
        break
    elif zad == "1":
        show_tasks()
    elif zad == "2":
        add_tasks()
    elif zad == "4":
        delete_tasks()
    elif zad == "5":
        edit_tasks()
    elif zad == "6":
        clear_tasks()
    else:
        print("Такого пункта нет. введи 1-6.")