def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def umn(a, b):
    return a * b
def delen(a, b):
    if b == 0:
        return "На ноль делить нельзя! "
    return a / b

a = int(input("Первое число: "))
b = int(input("Второе число: "))
oper = input("Выберите действие (+, -, /, *): ")

if oper == "+":
    result = plus(a, b)
elif oper == "-":
    result = minus(a, b)
elif oper == "*":
    result = umn(a, b)
elif oper == "/":
    result = delen(a, b)
else:
    result = "Неизвестное действие! "

print(f"Результат: {result}")