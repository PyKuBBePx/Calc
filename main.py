import math
import time
# Оганнисян Артур Сааквич УБВТ-2102 Вариант 2
def my_decorator(func):
    def decor(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        print(f"Была вызвана функция {func.__name__}\n"
              f"Время затраченное на выполение: {time.perf_counter() - start}")

    return decor

@my_decorator
def calc_area():
    n = int(input(
        "Введите количество сторон правильного многоугольника: "))  # Запрашивает у пользователя кол-во сторон правильного многоугольника.
    s = float(input(
        "Введите длину стороны правильного многоугольника: "))  # Заправшивает длину стороны у правильного многоуольника.
    area = (n * (s ** 2)) / (4 * math.tan((math.pi) / n))
    print("Площадь правильного многоугольника равна: ", area)

@my_decorator
def calc_numers():

    ar = list(map(int, input("Введите целые положительные числа: ").split()))
    num = input("Введите кол-во суммируемых чисел: ")
    num = int(num) + 1
    sum = 0
    i = 0
    for ar[i] in range(num):
        sum += int(ar[i])
    print("Сумма первых положительных чисел равна: ", sum)

def calc_alfavit():

    letter = input("Введите букву латинского алфавита: ")
    if letter == "a" or letter == "e" or \
            letter == "i" or letter == "o" or \
            letter == "u":
        print("- гласная буква.")
    elif letter == "y":\
        print("- и согласная, и гласная буква.")
    else:
        print(" - согласная буква.")


calc_alfavit()
calc_area()
calc_numers()
