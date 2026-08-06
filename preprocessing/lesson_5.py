import random

random_lisy = [random.randint(-50, 150) for i in range(10)]
print(random_lisy, sep= ", ")
random_list = []
for i in random_lisy:
    if 0 <= i <= 100:
        random_list.append(i)
print(random_list, sep=', ')
