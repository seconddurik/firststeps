contacts = {}

print("Телефонная книга")

while True:
    print("\n--- МЕНЮ ---")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Показать все контакты")
    print("5. Закрыть телефонную книгу")

    choice = input("Выберите действие:")

    if choice == "1":
        name = input("Имя: ")
        if name in contacts:
            print("Такой контакт уже есть, используйте другое имя!")
        else:
            phone = input("Номер: ")
            contacts[name] = phone
            print(f"Контакт {name} успешно добавлен!")
    
    elif choice == "2":
        name = input("Кого найти? ")
        phone = contacts.get(name)
        if phone:
            print(f"Номер {name}: {phone}")
        else:
            print("Контакт не найден. ")
    
    elif choice == "3":
        name = input("Кого удалять? ")
        if name in contacts:
            del contacts[name]
            print(f"Контакт {name} удалён! ")
        else:
            print("Контакт не найден! ")

    elif choice == "4":
        if not contacts:
            print("Телефонная книга пуста! ")
        else:
            print("--- Все контакты: --- ")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "5":
        print("До встречи, сэр!")
        break

    else:
        print("Нет такого пункта! ")