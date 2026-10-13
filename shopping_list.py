shopping = []
print("Добро пожаловать в менеджер покупок, сэр!")

while True:
    print("\n--- МЕНЮ ---")
    print("1. Показать список")
    print("2. Добавить товар")
    print("3. Удалить товар")
    print("4. Выход")

    choice = input("Выберите действие (1-4), сэр:")

    if choice == "1":
        if len(shopping) == 0:
            print("Список пуст!")
        else:
            print(f"В списке '{len(shopping)}' товаров:")
            for item in shopping:
                print(f" - {item}")

    elif choice == "2":
        new_item = input("Что добавить, сэр? ")
        shopping.append(new_item)
        print(f"'{new_item}' успешно добавлен, сэр!")

    elif choice == "3":
        if len(shopping) == 0:
            print("Нечего удалять, сэр!")
        else:
            print("Текущий список, сэр:", shopping)
            item_to_remove = input("Какой товар удалить, сэр? ")
            if item_to_remove in shopping:
                shopping.remove(item_to_remove)
                print(f"'{item_to_remove}'удалён, сэр! ")
            else:
                print(f"'{item_to_remove}' нет в списке, сэр! ")

    elif choice == "4":
        print("До встречи, сэр!")
        break
    
    else:
        print("Сэр, такого пункта нет!")