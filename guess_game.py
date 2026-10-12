import random

secret_number = random.randint(1, 100)
attempts = 0
print("Э, ара, я загадал число от 1 до 100. Давай угадывай, да, э! ")

while True:
    guess = int(input("Твоё число, ара: "))
    attempts += 1

    if guess < secret_number:
        print("Не, брат, больше!")
    elif guess > secret_number:
        print("Не, брат, меньше!")
    else:
        print(f"Есть, брат! Попыток: {attempts}")
        break