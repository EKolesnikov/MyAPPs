import random

n = int(input("Введите колличество чисел в последовательности: "))
min = int(input("Введите минимальное число последователности: "))
max = int(input("Введите максимальное число последователности: "))


def funk():
    print("Случайно сгенерированная последовательность:")
    a = [random.randint(min, max) for _ in range(n)]
    print(a)
    print("Первое число последовательности : ", a[0])
    print("Последнее число последовательности : ", a[-1])


funk()
