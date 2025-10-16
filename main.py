def get_number(prompt):
    while True:
        try:
            return int(input(prompt))              # Проверяет что мы ввели число, а не другой какой-то символ
        except ValueError:
            print("Введите целое число.")

a = get_number("Введите первое число = ")
b = get_number("Введите второе число = ")          # Задаём значения числам "a" "b" и "с"
c = get_number("Введите третье число = ")

if a >= b and a >= c:
    go = a
elif b >= a and b >= c:                            # Производим проверку каждого значения с двумя другими
    go = b
else:
    go = c

print(f"Наибольшее число: {go}")                   # Выводим наибольшее значение

