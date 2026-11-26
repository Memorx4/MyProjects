import random

random_list = [random.randint(-20, 50) for i in range(12)]
print(random_list, sep=", ")
freezing = []
hot = []
for i in random_list:
    if i <= 0:
        freezing.append(i)
    else:
        hot.append(i)
print(freezing, sep=", ")
print(hot)