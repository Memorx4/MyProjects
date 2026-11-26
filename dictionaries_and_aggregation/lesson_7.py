import random

random_list = [random.randint(-5000, 5000) for i in range(10)]
print(random_list, sep=', ')
negativ = 0
positiv = 0
zero = 0
for i in random_list:
    if i > 0:
        positiv += 1
    elif i < 0:
        negativ += 1
    else:
        zero += 1
print(positiv, negativ, zero)