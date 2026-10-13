numbers = [1, 5, 8, 7]
print("Исходный вариант:", numbers)

numbers.sort()
print("По возрастанию:", numbers)

numbers.reverse()
print("По убыванию:", numbers)

removed = numbers.pop(3)
print("Удалили число:", removed)
print("Числа, после удаления:", numbers)

numbers.insert(2, 27)
print("После вставки:", numbers)

print("Первые три:", numbers[::3])
print("Через срез наоборот:", numbers[::-1])