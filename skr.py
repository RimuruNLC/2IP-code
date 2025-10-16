import random


def slot_machine():
    balance = 200
    print("Добро пожаловать в слот-машину! Начальный баланс: $100")

    while True:
        print(f"\nВаш баланс: ${balance}")
        bet = int(input("Введите ставку (или 0 для выхода): "))
        if bet == 0:
            print("Спасибо за игру! Удачи!")
            break
        if bet > balance:
            print("Недостаточно средств.")
            continue

        # Генерируем три случайных числа от 1 до 10
        slots = [random.randint(2, 7) for _ in range(3)]
        print("Результат: ", slots)

        # Подсчет совпадений
        counts = {}
        for num in slots:
            counts[num] = counts.get(num, 0) + 1

        max_count = max(counts.values())

        if max_count == 3:
            # Все три одинаковые - выигрыш 4x
            winnings = bet * 4
            balance += winnings
            print(f"Три совпадения! Вы выиграли ${winnings}.")
        elif max_count == 2:
            # Два совпадения - выигрыш 2x
            winnings = bet * 2
            balance += winnings
            print(f"Два совпадения! Вы выиграли ${winnings}.")
        else:
            # Нет совпадений - проигрыш ставки
            balance -= bet
            print("Нет совпадений. Вы проиграли ставку.")

        if balance <= 0:
            print("У вас закончились деньги. Игра окончена.")
            break


slot_machine()