import random


def my_function():
    a = random.sample(range(20), 10)
    print("список а:"+str(a))
    b = random.sample(range(20), 10)
    print("список b:"+str(b))
    result = list(set(a) & set(b))
    print("общие елементы для двох списков:"+str(result))


my_function()
