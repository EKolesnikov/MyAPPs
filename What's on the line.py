def counter(str, chr):
    count = 0
    for i in range(len(str)):
       if str[i] == chr:
           count += 1
    return count

str = input("Введите текст: ").lower()
chr = input("Введите букву: ").lower()
print("Буква {0} встречается {1} раз".format(chr, counter(str, chr)))
