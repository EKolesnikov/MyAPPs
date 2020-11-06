a = int(input("Введите число:"))


def my_function(a):
    b = [int(x) for x in str(a)]
    result = sum(b)
    print("Сумма елементов введенного числа составляет:"+str(result))


my_function(a)
