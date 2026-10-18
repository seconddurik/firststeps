tasks = []

while True:
    print("1. Показать задачи\n2. Добавить задачу\n3. Выход\n4. Удалить задачу")
    
    zad = input("Выберите число (1-3): ")
    
    if zad == "3":
        print("Всего доброго!")
        break
    elif zad == "1":
        print("Ваши задачи: ")
    for task in tasks:
        print(task)
    if not tasks:
            print("Список пуст!")
    elif zad == "2":
        new_task = input("Что добавить? ")
        tasks.append(new_task)
        print("Задача добавлена!")
    elif zad == "4":
        print("Ваши задачи: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        choice = input("Какую задачу удаляем? (введите номер): ")
        if not choice.isdigit():
            print("Ошибка! Нужно ввести число! ")
        else:
            choice_num = int(choice)
            if 1 <= choice_num <= len (tasks):
                deleted_task = tasks.pop(choice_num - 1)
                print(f"Задача '{deleted_task}' успешно удалена! ")
            else:
                print("Задачи с таким порядковым номером не существует! ")