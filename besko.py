def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите целое число.")

# Запрашиваем количество чисел, которые пользователь хочет ввести
count = get_number("Сколько чисел вы хотите ввести? ")

numbers = []

for i in range(count):
    num = get_number(f"Введите число {i + 1}: ")
    numbers.append(num)

# Находим максимум среди введённых чисел
max_number = max(numbers)

print(f"Наибольшее число: {max_number}")