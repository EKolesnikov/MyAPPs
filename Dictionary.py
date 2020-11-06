def func1(a, b):
    return {a: b}


a = input("Введите ключ для первого словаря:")
b = input("Введите значение для первого словаря:")
dict1 = func1(a, b)


def func2(c, d):
    return {c: d}


c = input("Введите ключ для второго словаря:")
d = input("Введите значение для второго словаря:")
dict2 = func2(c, d)


def dict_3(dict1, dict2):
    return{**dict1, **dict2}


print(dict_3(dict1, dict2))
