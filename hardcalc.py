a = int(input("Первое число: "))
b = int(input("Второе число: "))
operation = input("Действие (+, -, *, /): ")

if operation == "+":
    print(f"{a} + {b} = {a + b}")
elif operation == "-":
    print(f"{a} + {b} = {a - b}")
elif operation == "*":
    print(f"{a} * {b} = {a * b}")
elif operation == "/":
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print(f"{a} / {b} = {a / b}")
else:
    print("Я не знаю такого действия.")