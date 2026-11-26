import random

random_list = [random.randint(-50, 1000000) for i in range(100)]
print(random_list, sep=', ')
new_list =[]
for i in random_list:
    if 0 < i < 100000000:
        new_list.append(i)
print(new_list, sep=', ')