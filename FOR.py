import random
list = random.sample(range(10), 5)
for x in list:
    print(x)
if 3 in list:
    res = "the digit 3 is in the list under the # {}."
    print(res.format(list.index(3)))
else:
    print("The digit 3 is missing")
